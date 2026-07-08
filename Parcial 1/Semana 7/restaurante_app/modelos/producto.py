"""
Módulo producto.py - Contiene la clase Producto
Descripción: Define la clase Producto con constructor tradicional (__init__),
decoradores @property y @setter para controlar acceso y modificación de atributos.
"""


class Producto:
    """
    Clase que representa un producto del restaurante.

    Atributos:
    - _nombre: nombre del producto (privado)
    - _categoria: categoría del producto (privado)
    - _precio: precio del producto en moneda local (privado)
    - _disponible: estado de disponibilidad del producto (privado)

    Requisitos:
    - El nombre no puede estar vacío
    - La categoría no puede estar vacía
    - El precio debe ser mayor que cero
    """

    def __init__(self, nombre, categoria, precio, disponible=True):
        """
        Constructor tradicional de la clase Producto.

        Args:
            nombre (str): Nombre del producto
            categoria (str): Categoría del producto (Bebida, Platillo, Postre, etc.)
            precio (float): Precio del producto
            disponible (bool): Disponibilidad del producto (por defecto True)

        Raises:
            ValueError: Si los datos no cumplen las validaciones
        """
        self._nombre = None
        self._categoria = None
        self._precio = None
        self._disponible = disponible

        # Usar los setters para validar los datos al crear el objeto
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    # PROPIEDADES Y SETTERS PARA NOMBRE
    @property
    def nombre(self):
        """Obtiene el nombre del producto."""
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        """
        Establece el nombre del producto con validación.

        Validación: El nombre no puede estar vacío
        """
        if not valor or not str(valor).strip():
            raise ValueError("❌ Error: El nombre del producto no puede estar vacío.")
        self._nombre = str(valor).strip()

    # PROPIEDADES Y SETTERS PARA CATEGORÍA
    @property
    def categoria(self):
        """Obtiene la categoría del producto."""
        return self._categoria

    @categoria.setter
    def categoria(self, valor):
        """
        Establece la categoría del producto con validación.

        Validación: La categoría no puede estar vacía
        """
        if not valor or not str(valor).strip():
            raise ValueError("❌ Error: La categoría del producto no puede estar vacía.")
        self._categoria = str(valor).strip()

    # PROPIEDADES Y SETTERS PARA PRECIO
    @property
    def precio(self):
        """Obtiene el precio del producto."""
        return self._precio

    @precio.setter
    def precio(self, valor):
        """
        Establece el precio del producto con validación.

        Validación: El precio debe ser mayor que cero
        """
        try:
            precio_float = float(valor)
            if precio_float <= 0:
                raise ValueError("❌ Error: El precio debe ser mayor que cero.")
            self._precio = precio_float
        except ValueError as e:
            if "mayor que cero" in str(e):
                raise e
            raise ValueError("❌ Error: El precio debe ser un número válido.")

    # PROPIEDADES Y SETTERS PARA DISPONIBILIDAD
    @property
    def disponible(self):
        """Obtiene el estado de disponibilidad del producto."""
        return self._disponible

    @disponible.setter
    def disponible(self, valor):
        """Establece el estado de disponibilidad del producto."""
        self._disponible = bool(valor)

    def mostrar_informacion(self):
        """
        Muestra la información del producto de forma legible.

        Retorna:
            str: Información formateada del producto
        """
        estado = "✅ Disponible" if self._disponible else "❌ No disponible"
        informacion = (
            f"\n{'='*50}\n"
            f"📦 INFORMACIÓN DEL PRODUCTO\n"
            f"{'='*50}\n"
            f"Nombre:       {self._nombre}\n"
            f"Categoría:    {self._categoria}\n"
            f"Precio:       ${self._precio:.2f}\n"
            f"Estado:       {estado}\n"
            f"{'='*50}\n"
        )
        return informacion

    def __str__(self):
        """Representación en string del producto."""
        estado = "✅" if self._disponible else "❌"
        return f"{estado} {self._nombre} ({self._categoria}) - ${self._precio:.2f}"

    def __repr__(self):
        """Representación técnica del producto."""
        return f"Producto(nombre='{self._nombre}', categoria='{self._categoria}', precio={self._precio}, disponible={self._disponible})"

