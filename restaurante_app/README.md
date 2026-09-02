# restaurante_app - Semana 12

Estudiante: Fernando Fernández

## Descripción del sistema
Se mantiene la aplicación de gestión del restaurante desarrollada en semanas anteriores, con persistencia en JSON, control de stock y relación `Usuario + Producto -> Venta`, pero incorporando optimizaciones de rendimiento mediante colecciones auxiliares en memoria.

La mejora principal consiste en evitar recorridos completos de listas cuando ya existe una clave única conocida, como el código del producto o la identificación del usuario.

## Mejoras aplicadas
- Se conservan las listas principales `self._productos`, `self._usuarios` y `self._ventas` para almacenar, recorrer y persistir objetos.
- Se agregan índices en memoria con `dict` para búsquedas rápidas:
  - `self._productos_por_codigo`
  - `self._usuarios_por_identificacion`
  - `self._ventas_por_usuario`
- La consulta de ventas por usuario ya no recorre toda la colección de ventas cada vez: se accede directamente por clave.
- Se reconstruyen los índices al inicializar el servicio a partir de los datos cargados desde JSON, manteniendo coherencia tras reinicios.
- Se mantiene sincronización de índices al registrar, eliminar y vender productos, sin dejar de usar la colección principal del sistema.
- Se sigue usando `set` de forma segura para obtener categorías únicas mediante comprensión, sin reemplazar el modelo por diccionarios.

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

## Colecciones utilizadas
- `list`: almacena productos, usuarios y ventas para persistir y listar registros.
- `dict`: acelera búsquedas por código de producto, identificación de usuario y consulta de ventas por usuario.
- `set`: obtiene categorías únicas sin duplicados.

## Cómo ejecutar
Desde la carpeta `restaurante_app`:

```bash
python main.py
```

## Pruebas principales realizadas
- Registro de producto y usuario.
- Búsqueda rápida de producto por código.
- Búsqueda rápida de usuario por identificación.
- Consulta de ventas por usuario usando el índice auxiliar.
- Venta válida con actualización del stock.
- Verificación de coherencia de índices tras registrar, modificar y eliminar información.
- Reinicio del sistema y reconstrucción de índices desde los archivos JSON.

## Resultado esperado
La aplicación sigue funcionando igual que en la Semana 11, pero con búsquedas y consultas más eficientes al usar estructuras auxiliares de tipo `dict` sin perder la claridad del diseño modular.
