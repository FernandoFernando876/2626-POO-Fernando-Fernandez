import json
from pathlib import Path

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.usuario import Usuario

print('--- Inicio de simulación automática ---')

archivo = ArchivoServicio()
productos = archivo.cargar_productos()
usuarios = archivo.cargar_usuarios()
ventas = archivo.cargar_ventas()

print(f'Productos cargados: {len(productos)}')
print(f'Usuarios cargados: {len(usuarios)}')
print(f'Ventas cargadas: {len(ventas)}')

rest = Restaurante(productos=productos, usuarios=usuarios, ventas=ventas)

# Registrar usuario de prueba
uid = 'u1'
if rest.obtener_usuario(uid) is None:
    usuario = Usuario(identificacion=uid, nombre='Usuario Prueba', correo='prueba@example.com')
    rest.registrar_usuario(usuario)
    archivo.guardar_usuarios(rest.obtener_usuarios())
    print(f'Usuario {uid} registrado.')
else:
    print(f'Usuario {uid} ya existe.')

# Registrar producto de prueba
codigo = 'p1'
producto = rest.obtener_producto(codigo)
if producto is None:
    producto = Producto(codigo=codigo, nombre='Hamburguesa', categoria='Comida', precio=10.0, stock=5)
    rest.registrar_producto(producto)
    archivo.guardar_productos(rest.obtener_productos())
    print(f'Producto {codigo} registrado con stock 5.')
else:
    producto.stock = 5
    archivo.guardar_productos(rest.obtener_productos())
    print(f'Producto {codigo} existente: stock actualizado a 5.')

# Venta válida
print('\nIntentando venta válida (cantidad 2)...')
res = rest.vender_producto(codigo, uid, 2)
if res:
    archivo.guardar_ventas(rest.obtener_ventas())
    archivo.guardar_productos(rest.obtener_productos())
    print('Venta válida registrada correctamente.')
else:
    print('La venta válida fue rechazada (error).')

# Estado después de venta válida
p = rest.obtener_producto(codigo)
print(f'Stock después de venta válida: {p.stock if p is not None else "(producto no existe)"}')

# Venta inválida (mayor al stock)
print('\nIntentando venta inválida (cantidad 10)...')
res2 = rest.vender_producto(codigo, uid, 10)
if not res2:
    print('Venta inválida correctamente rechazada.')
else:
    print('Venta inválida fue registrada (error).')

# Estado final
p = rest.obtener_producto(codigo)
print(f'Stock final: {p.stock if p is not None else "(producto no existe)"}')

print('\nVentas en memoria:')
for v in rest.obtener_ventas():
    print('-', v.to_dict())

# Mostrar contenido de archivos JSON para ver persistencia
base = Path(__file__).resolve().parent / 'datos'
for name in ('productos.json', 'usuarios.json', 'ventas.json'):
    path = base / name
    print(f'\nContenido de {name}:')
    try:
        with path.open('r', encoding='utf-8') as f:
            data = json.load(f)
            print(json.dumps(data, ensure_ascii=False, indent=2))
    except FileNotFoundError:
        print('  (archivo no encontrado)')
    except json.JSONDecodeError as e:
        print(f'  (JSON inválido: {e})')

print('\n--- Fin de simulación ---')
