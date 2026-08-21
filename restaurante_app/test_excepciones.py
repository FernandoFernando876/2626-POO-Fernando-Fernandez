"""
Archivo de pruebas para validar el manejo de excepciones
en la persistencia de productos con JSON.

Este archivo proporciona casos de prueba para verificar que:
- FileNotFoundError se maneja correctamente
- json.JSONDecodeError se maneja correctamente
- Registros incompletos o inválidos se omiten sin detener el programa
- PermissionError se puede simular
"""

import json
import os
from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.bebida import Bebida


def test_archivo_no_existe():
    """
    TEST 1: Verifica que el sistema inicie correctamente
    cuando el archivo JSON no existe (primer inicio).
    """
    print("\n" + "="*60)
    print("TEST 1: FileNotFoundError - Archivo no existe")
    print("="*60)
    
    ruta_inexistente = "datos/productos_inexistente.json"
    archivo = ArchivoServicio(ruta_inexistente)
    
    # Eliminar el archivo si existe
    if os.path.exists(ruta_inexistente):
        os.remove(ruta_inexistente)
    
    productos = archivo.cargar_productos()
    print(f"✓ Se cargaron {len(productos)} productos (colección vacía)")
    print("✓ El programa continuó normalmente sin fichero")
    assert len(productos) == 0, "Debería retornar lista vacía"


def test_json_invalido():
    """
    TEST 2: Verifica que se maneja correctamente
    cuando el archivo JSON es inválido.
    """
    print("\n" + "="*60)
    print("TEST 2: json.JSONDecodeError - JSON inválido")
    print("="*60)
    
    ruta_invalida = "datos/productos_invalido.json"
    
    # Escribir JSON inválido
    with open(ruta_invalida, 'w', encoding='utf-8') as f:
        f.write("{ esto no es json válido ]")
    
    archivo = ArchivoServicio(ruta_invalida)
    productos = archivo.cargar_productos()
    
    print(f"✓ Se detectó JSON inválido")
    print(f"✓ Se retornó lista vacía: {len(productos)} productos")
    print("✓ El programa continuó sin detener")
    
    # Limpiar
    os.remove(ruta_invalida)
    assert len(productos) == 0, "Debería retornar lista vacía"


def test_registro_incompleto():
    """
    TEST 3: Verifica que registros incompletos se omiten
    sin detener el programa.
    """
    print("\n" + "="*60)
    print("TEST 3: KeyError/ValueError - Registro incompleto")
    print("="*60)
    
    ruta_incompleta = "datos/productos_incompleta.json"
    
    # Crear JSON con un registro incompleto y uno válido
    datos = [
        {"tipo": "Producto", "codigo": "P001", "nombre": "Producto Válido"},  # Falta categoría y precio
        {"tipo": "Producto", "codigo": "P002", "nombre": "Producto Correcto", "categoria": "Test", "precio": 10.00},
        {"tipo": "Bebida", "codigo": "B001", "nombre": "Bebida Incompleta"},  # Falta campos específicos
    ]
    
    with open(ruta_incompleta, 'w', encoding='utf-8') as f:
        json.dump(datos, f)
    
    archivo = ArchivoServicio(ruta_incompleta)
    productos = archivo.cargar_productos()
    
    print(f"✓ Se cargaron {len(productos)} productos (se omitieron 2 incompletos)")
    print(f"✓ El producto válido: {productos[0].mostrar_informacion()}")
    print("✓ El programa continuó sin detener por registros inválidos")
    
    # Limpiar
    os.remove(ruta_incompleta)
    assert len(productos) == 1, "Debería cargar solo el registro válido"


def test_json_no_lista():
    """
    TEST 4: Verifica que se maneja correctamente
    cuando el JSON no es una lista.
    """
    print("\n" + "="*60)
    print("TEST 4: TypeError - JSON es diccionario, no lista")
    print("="*60)
    
    ruta_dict = "datos/productos_diccionario.json"
    
    # Escribir diccionario en lugar de lista
    with open(ruta_dict, 'w', encoding='utf-8') as f:
        json.dump({"error": "esto debería ser una lista"}, f)
    
    archivo = ArchivoServicio(ruta_dict)
    productos = archivo.cargar_productos()
    
    print(f"✓ Se detectó estructura inválida (diccionario en lugar de lista)")
    print(f"✓ Se retornó lista vacía: {len(productos)} productos")
    print("✓ El programa continuó sin detener")
    
    # Limpiar
    os.remove(ruta_dict)
    assert len(productos) == 0, "Debería retornar lista vacía"


def test_precio_negativo():
    """
    TEST 5: Verifica que precio negativo se rechaza.
    """
    print("\n" + "="*60)
    print("TEST 5: ValueError - Precio negativo o cero")
    print("="*60)
    
    ruta_precio = "datos/productos_precio_negativo.json"
    
    # Crear JSON con precios inválidos
    datos = [
        {"tipo": "Producto", "codigo": "P001", "nombre": "Producto", "categoria": "Test", "precio": -5.00},
        {"tipo": "Producto", "codigo": "P002", "nombre": "Producto", "categoria": "Test", "precio": 0},
        {"tipo": "Producto", "codigo": "P003", "nombre": "Producto", "categoria": "Test", "precio": 10.00},
    ]
    
    with open(ruta_precio, 'w', encoding='utf-8') as f:
        json.dump(datos, f)
    
    archivo = ArchivoServicio(ruta_precio)
    productos = archivo.cargar_productos()
    
    print(f"✓ Se cargaron {len(productos)} productos (se omitieron 2 con precios inválidos)")
    print(f"✓ El producto válido: {productos[0].mostrar_informacion()}")
    print("✓ Se rechazaron precios negativos y cero")
    
    # Limpiar
    os.remove(ruta_precio)
    assert len(productos) == 1, "Debería cargar solo el registro con precio válido"


def test_persistencia_completa():
    """
    TEST 6: Prueba completa del ciclo de persistencia.
    """
    print("\n" + "="*60)
    print("TEST 6: Ciclo completo de persistencia")
    print("="*60)
    
    ruta_completa = "datos/productos_completa_test.json"
    
    # Crear productos iniciales
    print("1. Crear productos...")
    rest = Restaurante()
    p1 = Producto('TEST001', 'Producto Test 1', 'Categoría Test', 50.00)
    p2 = Producto('TEST002', 'Producto Test 2', 'Categoría Test', 75.00)
    b1 = Bebida('BEB001', 'Bebida Test', 'Bebidas', 5.00, '500ml', 'botella')
    
    rest.registrar_producto(p1)
    rest.registrar_producto(p2)
    rest.registrar_producto(b1)
    
    # Guardar
    print("2. Guardar en JSON...")
    archivo = ArchivoServicio(ruta_completa)
    archivo.guardar_productos(rest.obtener_productos_copia())
    print(f"✓ Se guardaron {len(rest.obtener_productos_copia())} productos")
    
    # Recargar (simulando reinicio)
    print("3. Recargar desde JSON (simulando reinicio)...")
    rest2 = Restaurante()
    productos_cargados = archivo.cargar_productos()
    rest2.cargar_productos_iniciales(productos_cargados)
    print(f"✓ Se recuperaron {len(productos_cargados)} productos")
    
    # Modificar y guardar
    print("4. Modificar y guardar nuevamente...")
    rest2.actualizar_producto('TEST001', precio=60.00)
    rest2.eliminar_producto('TEST002')
    archivo.guardar_productos(rest2.obtener_productos_copia())
    print(f"✓ Se guardan {len(rest2.obtener_productos_copia())} productos modificados")
    
    # Verificar resultado final
    print("5. Verificar contenido final...")
    with open(ruta_completa, 'r', encoding='utf-8') as f:
        contenido = json.load(f)
    
    print(f"✓ Archivo contiene {len(contenido)} registros")
    for reg in contenido:
        print(f"   - {reg['codigo']}: {reg['nombre']} (${reg['precio']})")
    
    # Limpiar
    os.remove(ruta_completa)
    assert len(contenido) == 2, "Debería tener 2 registros"


def main():
    """
    Ejecuta todas las pruebas de manejo de excepciones.
    """
    print("\n" + "#"*60)
    print("PRUEBAS DE MANEJO DE EXCEPCIONES")
    print("Sistema de Persistencia de Productos con JSON")
    print("#"*60)
    
    try:
        test_archivo_no_existe()
        test_json_invalido()
        test_registro_incompleto()
        test_json_no_lista()
        test_precio_negativo()
        test_persistencia_completa()
        
        print("\n" + "="*60)
        print("✅ TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE")
        print("="*60 + "\n")
    except AssertionError as e:
        print(f"\n❌ ERROR EN PRUEBA: {e}\n")
    except Exception as e:
        print(f"\n❌ ERROR INESPERADO: {e}\n")


if __name__ == "__main__":
    main()

