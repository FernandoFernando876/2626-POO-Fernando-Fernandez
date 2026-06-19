# Clase que representa un cliente del restaurante
class Cliente:
    """
    Representa un cliente que realiza pedidos en el restaurante.

    Atributos:
        id (int): Identificador único del cliente
        nombre (str): Nombre completo del cliente
        email (str): Correo electrónico del cliente
        telefono (str): Número de teléfono del cliente
        activo (bool): Indica si el cliente es activo
    """

    def __init__(self, id, nombre, email, telefono):
        """
        Inicializa un nuevo cliente.

        Args:
            id: Identificador único del cliente
            nombre: Nombre completo del cliente
            email: Correo electrónico del cliente
            telefono: Número de teléfono del cliente
        """
        self.id = id
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.activo = True
        self.pedidos_realizados = 0

    def __str__(self):
        """Representación en texto del cliente."""
        estado = "Activo" if self.activo else "Inactivo"
        return f"[{self.id}] {self.nombre}\n    Email: {self.email}\n    Teléfono: {self.telefono}\n    Estado: {estado}"

    def desactivar_cliente(self):
        """Desactiva el cliente."""
        self.activo = False

    def activar_cliente(self):
        """Activa el cliente."""
        self.activo = True

    def registrar_pedido(self):
        """Incrementa el contador de pedidos realizados."""
        self.pedidos_realizados += 1

    def obtener_informacion(self):
        """Retorna la información del cliente de forma detallada."""
        return {
            'id': self.id,
            'nombre': self.nombre,
            'email': self.email,
            'telefono': self.telefono,
            'activo': self.activo,
            'pedidos_realizados': self.pedidos_realizados
        }

