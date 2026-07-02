# Módulo: modelos/__init__.py
# Descripción: Inicializador del paquete de modelos del restaurante

from .producto import Producto
from .platillo import Platillo
from .bebida import Bebida

__all__ = ['Producto', 'Platillo', 'Bebida']
