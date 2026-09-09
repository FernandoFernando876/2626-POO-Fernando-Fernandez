# restaurante_app - Semana 12

Estudiante: Fernando Fernández

## Descripción del sistema
Se conserva la aplicación de gestión del restaurante desarrollada en semanas anteriores, con persistencia en JSON, control de stock y relación `Usuario + Producto -> Venta`, pero aplicando optimizaciones usando colecciones auxiliares en memoria.

La mejora principal consiste en evitar recorridos completos sobre listas cuando ya existe una clave conocida, como el código del producto o la identificación del usuario.

## Mejoras aplicadas
- Se mantienen las listas principales `self._productos`, `self._usuarios` y `self._ventas` para almacenar, recorrer y persistir objetos.
- Se agregan índices con `dict` para búsquedas frecuentes:
  - `self._productos_por_codigo`
  - `self._usuarios_por_identificacion`
  - `self._ventas_por_usuario`
- La consulta de ventas por usuario ya no recorre toda la colección de ventas cada vez; se accede por clave.
- Los índices se reconstruyen al iniciar desde los datos de JSON.
- Los índices se mantienen sincronizados al registrar, eliminar y vender.
- Se mantiene `set` para categorías únicas sin duplicados.

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
- `list`: almacena productos, usuarios y ventas.
- `dict`: mejora búsquedas por clave y consultas de ventas por usuario.
- `set`: obtiene categorías sin duplicados.

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
- Verificación de coherencia de índices tras registrar y eliminar información.
- Reinicio del sistema y reconstrucción de índices desde JSON.

## Resultado esperado
La aplicación sigue funcionando con la lógica de la Semana 11, pero con búsquedas y consultas más eficientes aplicando colecciones auxiliares en memoria sin perder la organización modular del proyecto.
