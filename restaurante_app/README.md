# restaurante_app - Semana 10

Estudiante: Fernando Fernández

## Descripción del sistema
Este proyecto evoluciona el sistema de administración de un restaurante para incluir persistencia real de productos mediante un archivo JSON. Durante la ejecución, las colecciones del sistema trabajan con objetos `Producto`, pero al cerrar la aplicación los datos se guardan en `datos/productos.json` y se vuelven a cargar al iniciar la sesión siguiente.

## Estructura del proyecto
restaurante_app/
├── datos/
│   └── productos.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
├── README.md

## Componentes principales
- `modelos/producto.py`: define la clase `Producto`, valida los campos obligatorios y convierte el objeto a un diccionario compatible con JSON.
- `modelos/usuario.py`: representa a un usuario del sistema y conserva la funcionalidad previa de gestión de usuarios.
- `servicios/restaurante.py`: administra la colección de productos y usuarios, así como las operaciones de registrar, buscar, actualizar, eliminar y listar.
- `servicios/archivo_servicio.py`: concentra la lectura y escritura de `productos.json` usando `with open()`, `json.load()` y `json.dump()`.
- `main.py`: crea los servicios, carga los productos existentes al iniciar la app y guarda los cambios luego de cada operación relevante.

## Persistencia en JSON
El archivo `datos/productos.json` almacenará la colección de productos como una lista de diccionarios. Cada producto se serializa con los campos `codigo`, `nombre`, `categoria` y `precio`. Al iniciar la aplicación, el contenido del archivo se carga y cada registro válido se convierte nuevamente en un objeto `Producto` para continuar usando la lógica del sistema sin perder la estructura orientada a objetos.

## Flujo de carga y guardado
1. `main.py` crea una instancia de `ArchivoServicio`.
2. Se intenta abrir y leer `datos/productos.json`.
3. Si el archivo existe y tiene un formato válido, se reconstruyen los objetos `Producto`.
4. El servicio `Restaurante` recibe la lista cargada y trabaja con esos objetos en memoria.
5. Cuando el usuario registra, actualiza o elimina un producto, `main.py` invoca el servicio correspondiente y luego solicita guardar la colección de nuevo en `productos.json`.

## Manejo de excepciones
Se controlan las situaciones esperadas del acceso a archivos y la validación de datos:
- `FileNotFoundError`: se maneja para permitir que el programa inicie con una colección vacía si el archivo aún no existe.
- `json.JSONDecodeError`: se detecta cuando el archivo está presente pero no contiene JSON válido.
- `PermissionError`: se controla para evitar que un problema de permisos detenga la aplicación.
- `KeyError`: se usa al reconstruir productos con registros incompletos o sin claves esperadas.
- `ValueError`: se utiliza en la validación propia de `Producto` para descartar o bloquear entradas inválidas sin romper el flujo principal.

## Cómo ejecutar el proyecto
Desde la carpeta `restaurante_app`, ejecuta:

```bash
python main.py
```

## Verificación de persistencia
Se comprobó que los productos siguen disponibles después de cerrar y volver a ejecutar la aplicación. La prueba consistió en:
1. registrar uno o más productos desde el menú,
2. verificar que `datos/productos.json` contenía la información,
3. cerrar la aplicación,
4. volver a ejecutarla,
5. listar los productos y confirmar que los datos habían sido recuperados,
6. actualizar o eliminar un producto y volver a iniciar para comprobar que la modificación también quedó guardada.

Con este flujo, la estructura de objetos de dominio se conserva en memoria y la persistencia se gestiona de forma separada en el servicio de archivos.
