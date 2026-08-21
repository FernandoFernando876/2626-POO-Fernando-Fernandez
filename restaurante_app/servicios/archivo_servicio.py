import json
import os
from typing import List, Dict, Any
from modelos.producto import Producto
from modelos.bebida import Bebida


class ArchivoServicio:
    """
    Servicio responsable de cargar y guardar productos desde/hacia un archivo JSON.
    Maneja excepciones específicas y valida la integridad de los datos.
    """

    def __init__(self, ruta_archivo: str) -> None:
        """
        Inicializa el servicio con la ruta del archivo JSON.

        Args:
            ruta_archivo: ruta absoluta o relativa al archivo productos.json
        """
        self.ruta_archivo: str = ruta_archivo

    def cargar_productos(self) -> List[Producto]:
        """
        Carga los productos desde el archivo JSON.
        Maneja excepciones específicas y devuelve una lista vacía si hay errores controlados.

        Excepciones controladas:
            - FileNotFoundError: archivo no existe (primer inicio normal)
            - json.JSONDecodeError: contenido no es JSON válido
            - PermissionError: sin permisos para leer
            - KeyError/ValueError: datos incompletos o inválidos

        Returns:
            Lista de objetos Producto reconstructed desde JSON.
        """
        if not os.path.exists(self.ruta_archivo):
            print(f"Archivo {self.ruta_archivo} no encontrado. Iniciando con colección vacía.")
            return []

        try:
            with open(self.ruta_archivo, 'r', encoding='utf-8-sig') as f:
                datos = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error: El archivo {self.ruta_archivo} no contiene JSON válido. Detalles: {e}")
            print("Iniciando con colección vacía. Revise manualmente el archivo JSON.")
            return []
        except PermissionError:
            print(f"Error: No tiene permisos para leer el archivo {self.ruta_archivo}.")
            print("Iniciando con colección vacía.")
            return []
        except Exception as e:
            print(f"Error inesperado al leer {self.ruta_archivo}: {e}")
            return []

        productos: List[Producto] = []

        # Validar que datos sea una lista
        if not isinstance(datos, list):
            print(f"Error: El archivo debe contener una lista JSON, no {type(datos).__name__}.")
            return []

        for idx, registro in enumerate(datos, start=1):
            try:
                producto = self._crear_producto_desde_diccionario(registro)
                if producto:
                    productos.append(producto)
            except (KeyError, ValueError, TypeError) as e:
                print(f"Advertencia: Registro #{idx} incompleto o inválido. Se omitirá. Detalles: {e}")
                continue

        print(f"Se cargaron {len(productos)} producto(s) desde {self.ruta_archivo}.")
        return productos

    def guardar_productos(self, productos: List[Producto]) -> bool:
        """
        Guarda la lista de productos en el archivo JSON.

        Args:
            productos: lista de objetos Producto a guardar

        Returns:
            True si se guardó correctamente, False en caso de error.
        """
        try:
            # Convertir cada producto a diccionario
            datos = [p.a_diccionario() for p in productos]

            # Crear directorio si no existe
            directorio = os.path.dirname(self.ruta_archivo)
            if directorio and not os.path.exists(directorio):
                os.makedirs(directorio, exist_ok=True)

            # Guardar con encoding UTF-8 e indentación para legibilidad
            with open(self.ruta_archivo, 'w', encoding='utf-8') as f:
                json.dump(datos, f, ensure_ascii=False, indent=2)

            return True
        except PermissionError:
            print(f"Error: No tiene permisos para escribir en {self.ruta_archivo}.")
            return False
        except Exception as e:
            print(f"Error al guardar productos en {self.ruta_archivo}: {e}")
            return False

    def _crear_producto_desde_diccionario(self, registro: Dict[str, Any]) -> Producto | None:
        """
        Reconstruye un objeto Producto (o Bebida) desde un diccionario.
        Valida que contenga los campos requeridos.

        Args:
            registro: diccionario con los datos del producto

        Returns:
            Objeto Producto o Bebida según el tipo, None si hay error.

        Raises:
            KeyError: si faltan campos obligatorios
            ValueError: si los datos son inválidos
        """
        # Campos obligatorios en todos los productos
        tipo = registro.get("tipo", "Producto")
        codigo = registro["codigo"]
        nombre = registro["nombre"]
        categoria = registro["categoria"]
        precio = float(registro["precio"])

        if not codigo or not nombre or not categoria or precio <= 0:
            raise ValueError(f"Producto con datos inválidos o incompletos: {registro}")

        if tipo == "Bebida":
            # Campos específicos de Bebida
            tamano = registro["tamano"]
            envase = registro["envase"]
            if not tamano or not envase:
                raise ValueError(f"Bebida con datos incompletos: {registro}")
            return Bebida(codigo=codigo, nombre=nombre, categoria=categoria, precio=precio, tamano=tamano, envase=envase)
        else:
            # Producto genérico
            return Producto(codigo=codigo, nombre=nombre, categoria=categoria, precio=precio)


