# restaurante_app - Semana 11

Estudiante: Fernando Fernández

## Descripción del sistema
Evolución del sistema de administración de un restaurante para incorporar:
- Persistencia en JSON de productos, usuarios y ventas.
- Control de stock por producto.
- Operación de venta que relaciona Usuario + Producto → Venta.

Se mantienen las colecciones como objetos de dominio (`Producto`, `Usuario`, `Venta`) y la lógica de negocio en el servicio `Restaurante`.

## Estructura del proyecto
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
└── README.md

## Componentes principales
- `modelos/producto.py`: ahora incluye el atributo `stock`, validaciones y el método `vender(cantidad)` que protege contra stock negativo.
- `modelos/usuario.py`: representacion de usuario y serialización/deserialización a JSON.
- `modelos/venta.py`: representa una venta con `usuario_id`, `producto_codigo` y `cantidad`.
- `servicios/restaurante.py`: administra productos, usuarios y ventas; implementa `vender_producto` y consultas de ventas por usuario.
- `servicios/archivo_servicio.py`: centraliza lectura/escritura de `productos.json`, `usuarios.json` y `ventas.json` usando `json.load()` y `json.dump()`.
- `main.py`: interfaz por consola para registrar productos/usuarios, realizar ventas y consultar ventas por usuario. Guarda las colecciones después de cada operación que las modifique.

## Stock y ventas
- Al registrar un producto se solicita el `stock` inicial.
- La operación de venta valida que el usuario exista, que el producto exista, que la cantidad sea válida y que haya stock suficiente.
- Si la venta es válida, se crea un objeto `Venta`, se agrega a la colección de ventas y se disminuye el stock del producto.
- Tras una venta correcta se guardan `ventas.json` y `productos.json`.

## Persistencia en JSON
- `productos.json`: lista de productos con su stock actualizado.
- `usuarios.json`: lista de usuarios registrados.
- `ventas.json`: lista de ventas realizadas.

Se controlan excepciones específicas: `FileNotFoundError`, `json.JSONDecodeError`, `PermissionError`, `KeyError` y `ValueError` para validar registros.

## Cómo ejecutar
Desde la carpeta `restaurante_app`:

```bash
python main.py
```

Usar el menú para registrar usuarios/productos, vender y consultar ventas. Tras cerrar y volver a ejecutar, los datos registrados deben recuperarse.

## Pruebas realizadas
- Registro de usuario y producto con stock
- Venta válida que disminuye el stock y queda registrada en `ventas.json`
- Intento de venta con cantidad mayor al stock: operación rechazada y datos sin cambios
- Reinicio de la aplicación: productos, usuarios y ventas se recuperan desde JSON


