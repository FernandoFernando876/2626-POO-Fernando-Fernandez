import sys
import os
# Asegurar que el paquete padre (restaurante_app) está en sys.path cuando se ejecuta el script
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from servicios.restaurante import Restaurante
from modelos.usuario import Usuario
from modelos.producto import Producto

def run_flow():
    r = Restaurante()

    print('--- Probar registro de usuario ---')
    u = Usuario('U1', 'Test User', 'test@example.com')
    added = r.registrar_usuario(u)
    print('registrar_usuario returned ->', added)
    print('listar_usuarios ->', r.listar_usuarios())

    print('\n--- Probar eliminación de usuario ---')
    removed = r.eliminar_usuario('U1')
    print("eliminar_usuario returned ->", removed)
    print('listar_usuarios after ->', r.listar_usuarios())

    print('\n--- Probar flujo de productos ---')
    p = Producto('P1', 'Pan', 'Alimentos', 5.0)
    print('registrar_producto ->', r.registrar_producto(p))
    print('listar_productos ->', r.listar_productos())
    print('buscar_producto P1 ->', r.buscar_producto('P1').mostrar_informacion())
    print('obtener_categorias_unicas ->', r.obtener_categorias_unicas())
    print('actualizar_producto ->', r.actualizar_producto('P1', nombre='Pan Integral', precio=6.5))
    print('listar_productos after update ->', r.listar_productos())
    print('eliminar_producto ->', r.eliminar_producto('P1'))
    print('listar_productos after delete ->', r.listar_productos())

if __name__ == '__main__':
    run_flow()


