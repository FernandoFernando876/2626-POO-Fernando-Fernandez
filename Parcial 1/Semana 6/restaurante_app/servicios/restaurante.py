# Módulo: restaurante.py
# Descripción: Clase de servicio que gestiona la lista de productos del restaurante y demuestra polimorfismo.

from typing import List, Optional, Tuple, Dict, Any
from modelos.producto import Producto

class Restaurante:
    """
    Clase de servicio encargada de administrar el menú de productos del restaurante.
    
    Atributos:
        nombre (str): Nombre del restaurante.
        lista_productos (List[Producto]): Lista de productos registrados en el restaurante.
    """

    def __init__(self, nombre: str):
        """
        Constructor de la clase Restaurante.

        Args:
            nombre: Nombre del restaurante.
        """
        self.nombre = nombre
        self.lista_productos: List[Producto] = []

    def agregar_producto(self, producto: Producto) -> None:
        """
        Agrega un producto (Platillo o Bebida) a la lista del restaurante.

        Args:
            producto: Objeto que hereda de la clase base Producto.
        """
        self.lista_productos.append(producto)
        print(f"[OK] Producto '{producto.nombre}' agregado exitosamente al menu.")

    def mostrar_menu(self) -> None:
        """
        Muestra la información de todos los productos registrados en el restaurante.
        Demuestra polimorfismo al llamar a mostrar_informacion() en objetos
        que pueden ser tanto Platillos como Bebidas.
        """
        print("\n" + "=" * 60)
        print(f"MENU DEL RESTAURANTE: {self.nombre.upper()}")
        print("=" * 60)
        
        if not self.lista_productos:
            print("El menú está vacío. Registre productos primero.")
            print("=" * 60 + "\n")
            return

        for index, producto in enumerate(self.lista_productos, start=1):
            # Aquí ocurre el Polimorfismo: se ejecuta mostrar_informacion() de Platillo o Bebida 
            # de forma transparente según el tipo real del objeto.
            print(f"Item #{index}:")
            print(producto.mostrar_informacion())
            print("-" * 45)
            
        print("=" * 60 + "\n")

    def buscar_producto(self, nombre: str) -> Optional[Producto]:
        """
        Busca un producto por su nombre (insensible a mayúsculas/minúsculas).

        Args:
            nombre: El nombre del producto a buscar.

        Returns:
            Optional[Producto]: El producto encontrado o None si no existe.
        """
        nombre_normalizado = nombre.strip().lower()
        for producto in self.lista_productos:
            if producto.nombre.strip().lower() == nombre_normalizado:
                return producto
        return None

    def obtener_estadisticas(self) -> Dict[str, Any]:
        """
        Calcula y retorna estadísticas completas sobre los productos del menú.

        Returns:
            Dict[str, Any]: Un diccionario con métricas del menú.
        """
        # Importaciones locales para evitar circularidad
        from modelos.platillo import Platillo
        from modelos.bebida import Bebida

        total_productos = len(self.lista_productos)
        if total_productos == 0:
            return {
                "total": 0,
                "platillos": 0,
                "bebidas": 0,
                "disponibles": 0,
                "agotados": 0,
                "promedio_precio": 0.0,
                "mas_caro": None,
                "mas_barato": None
            }

        platillos = sum(1 for p in self.lista_productos if isinstance(p, Platillo))
        bebidas = sum(1 for p in self.lista_productos if isinstance(p, Bebida))
        disponibles = sum(1 for p in self.lista_productos if p.disponible)
        agotados = total_productos - disponibles

        precios = [p.obtener_precio() for p in self.lista_productos]
        promedio = sum(precios) / total_productos

        mas_caro = max(self.lista_productos, key=lambda p: p.obtener_precio())
        mas_barato = min(self.lista_productos, key=lambda p: p.obtener_precio())

        return {
            "total": total_productos,
            "platillos": platillos,
            "bebidas": bebidas,
            "disponibles": disponibles,
            "agotados": agotados,
            "promedio_precio": promedio,
            "mas_caro": mas_caro,
            "mas_barato": mas_barato
        }

    def realizar_pedido(self, items_pedido: List[Tuple[str, int]]) -> Dict[str, Any]:
        """
        Procesa una lista de productos pedidos con sus respectivas cantidades.

        Args:
            items_pedido: Una lista de tuplas en el formato (nombre_producto, cantidad).

        Returns:
            Dict[str, Any]: Información consolidada de la transacción y errores de stock.
        """
        items_procesados = []
        errores = []
        subtotal = 0.0

        for nombre_prod, cantidad in items_pedido:
            if cantidad <= 0:
                errores.append(f"{nombre_prod} (Cantidad '{cantidad}' no válida)")
                continue

            producto = self.buscar_producto(nombre_prod)
            if not producto:
                errores.append(f"{nombre_prod} (Producto no encontrado en el menú)")
            elif not producto.disponible:
                errores.append(f"{producto.nombre} (Producto agotado/no disponible)")
            else:
                precio_unitario = producto.obtener_precio()
                total_item = precio_unitario * cantidad
                subtotal += total_item
                items_procesados.append({
                    "producto": producto,
                    "cantidad": cantidad,
                    "precio_unitario": precio_unitario,
                    "total_item": total_item
                })

        igv = subtotal * 0.18
        total = subtotal + igv

        return {
            "items_procesados": items_procesados,
            "errores": errores,
            "subtotal": subtotal,
            "igv": igv,
            "total": total
        }

    def imprimir_recibo(self, pedido_info: Dict[str, Any]) -> None:
        """
        Imprime un recibo de venta con formato profesional a partir de la información del pedido.

        Args:
            pedido_info: El diccionario retornado por realizar_pedido().
        """
        print("\n" + "=" * 60)
        print("               BOLETA DE VENTA - CONSUMO")
        print("=" * 60)
        print(f" Establecimiento: {self.nombre.upper()}")
        print("-" * 60)
        print(f"{'Cant.':<6}{'Descripcion':<28}{'P.Unit.':<12}{'Total':<14}")
        print("-" * 60)

        for item in pedido_info["items_procesados"]:
            prod_name = item["producto"].nombre
            if len(prod_name) > 26:
                prod_name = prod_name[:23] + "..."
            
            print(f"{item['cantidad']:<6}{prod_name:<28}${item['precio_unitario']:<11.2f}${item['total_item']:<14.2f}")

        print("-" * 60)
        print(f"{'Subtotal:':<46}${pedido_info['subtotal']:>8.2f}")
        print(f"{'IGV (18%):':<46}${pedido_info['igv']:>8.2f}")
        print("-" * 60)
        print(f"{'TOTAL A PAGAR:':<46}${pedido_info['total']:>8.2f}")
        print("=" * 60)

        if pedido_info["errores"]:
            print("\n[ADVERTENCIA] No se pudieron procesar los siguientes items:")
            for err in pedido_info["errores"]:
                print(f"  * {err}")
            print("=" * 60)
        print()

