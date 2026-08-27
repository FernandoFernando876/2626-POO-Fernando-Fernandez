"""
Configuración de pytest: ajusta sys.path para encontrar módulos desde restaurante_app
"""
import sys
from pathlib import Path

# Añadir el directorio padre (restaurante_app) a sys.path
parent_dir = Path(__file__).parent.parent
sys.path.insert(0, str(parent_dir))

