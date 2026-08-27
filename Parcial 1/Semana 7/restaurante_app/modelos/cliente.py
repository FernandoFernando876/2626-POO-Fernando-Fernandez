"""
Módulo cliente.py - Contiene la clase Cliente
Descripción: Define la clase Cliente utilizando el decorador @dataclass
para una forma simplificada y elegante de crear la clase.
"""

from dataclasses import dataclass


@dataclass
class Cliente:
    """
    Clase que representa un cliente del restaurante.

    Utiliza el decorador @dataclass para reducir el boilerplate de código
    y proporcionar automáticamente métodos como __init__, __repr__, __eq__, etc.

    Atributos:
    - id_cliente (str): Identificador único del cliente
    - nombre (str): Nombre del cliente
    - correo (str): Correo electrónico del cliente
    """

    id_cliente: str
    nombre: str
    correo: str

    def mostrar_informacion(self):
        """
        Muestra la información del cliente de forma legible.

        Retorna:
            str: Información formateada del cliente
        """
        informacion = (
            f"\n{'='*50}\n"
            f"👤 INFORMACIÓN DEL CLIENTE\n"
            f"{'='*50}\n"
            f"ID Cliente:   {self.id_cliente}\n"
            f"Nombre:       {self.nombre}\n"
            f"Correo:       {self.correo}\n"
            f"{'='*50}\n"
        )
        return informacion

    def __str__(self):
        """Representación en string del cliente."""
        return f"👤 {self.nombre} (ID: {self.id_cliente}) - {self.correo}"

