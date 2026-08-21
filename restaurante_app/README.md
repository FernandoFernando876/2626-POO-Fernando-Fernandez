# Restaurante App - Semana 10: Persistencia de Productos con JSON

## Información General

**Estudiante:** [Tu nombre completo]  
**Semana:** 10 - Parcial 2  
**Curso:** Programación con Python  
**Fecha:** 2024

---

## Descripción del Sistema

El sistema **Restaurante App** es una aplicación de consola que administra productos y usuarios de un restaurante. Esta es la **Semana 10**, donde se incorpora la **persistencia de productos mediante archivos JSON**.

### Mejora Principal de la Semana 10

A diferencia de semanas anteriores donde los productos existían solo durante la ejecución del programa, ahora:

- ✅ Los productos se **guardan automáticamente** en un archivo JSON cada vez que se registra, actualiza o elimina uno
- ✅ Al iniciar el programa, se **cargan automáticamente** los productos almacenados
- ✅ Los datos **se mantienen entre ejecuciones**, permitiendo verdadera persistencia
- ✅ El sistema **maneja errores de archivo** de forma controlada
- ✅ Se validan estructuras JSON y datos incompletos sin detener la aplicación

---

## Estructura del Proyecto

```
restaurante_app/
├── datos/
│   └── productos.json          # Archivo de persistencia (se genera automáticamente)
├── modelos/
│   ├── __init__.py
│   ├── producto.py             # Clase Producto con método a_diccionario()
│   ├── bebida.py               # Clase Bebida (hereda de Producto)
│   └── usuario.py              # Clase Usuario (sin persistencia en esta semana)
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py     # Servicio de lectura/escritura JSON
│   └── restaurante.py          # Servicio de administración de productos y usuarios
├── main.py                     # Punto de entrada con menú interactivo
└── README.md                   # Este archivo
```

---

## Responsabilidad de Cada Componente

### `modelos/producto.py`

- Define la clase **Producto** con atributos: código, nombre, categoría, precio
- Proporciona el método **`a_diccionario()`** para convertir objetos a estructuras JSON-compatibles
- Implementa **`mostrar_informacion()`** para presentación en consola
- Mantiene todas las **validaciones** de datos

### `modelos/bebida.py`

- Hereda de **Producto** añadiendo atributos específicos: tamaño, envase
- Sobrescribe **`a_diccionario()`** para incluir campos adicionales
- Mantiene compatibilidad mediante polimorfismo

### `modelos/usuario.py`

- Define la clase **Usuario** con atributos: identificación, nombre, correo
- **No posee persistencia** en esta semana (permanece solo en memoria)
- Puede ser extendido en semanas futuras

### `servicios/archivo_servicio.py`

**Responsabilidades principales:**
- Cargar productos desde `datos/productos.json`
- Guardar productos en `datos/productos.json`
- Validar integridad de datos JSON
- Manejar excepciones específicas

**Excepciones controladas:**
- `FileNotFoundError`: Archivo no existe → inicia con colección vacía
- `json.JSONDecodeError`: JSON inválido → aviso y colección vacía
- `PermissionError`: Sin permisos → aviso y colección vacía
- `KeyError`: Registro incompleto → se omite el registro problemático
- `ValueError`: Datos inválidos → se omite el registro problemático

### `servicios/restaurante.py`

- Administra colecciones de **productos** y **usuarios** en memoria
- Proporciona métodos para **registrar, buscar, actualizar, eliminar** productos
- Método **`obtener_productos_copia()`** para entregar datos a persistencia
- Método **`cargar_productos_iniciales()`** para recibir datos desde archivo

### `main.py`

**Flujo de inicio:**
1. Crea instancia de **ArchivoServicio**
2. Carga productos desde JSON
3. Crea instancia de **Restaurante** e inicializa con productos cargados
4. Presenta menú interactivo

**Flujo tras operaciones con productos:**
1. Usuario realiza operación (registrar, actualizar, eliminar)
2. **Restaurante** modifica su colección en memoria
3. **main.py** solicita al **ArchivoServicio** guardar la colección
4. **ArchivoServicio** convierte productos a diccionarios y escribe JSON

---

## Funcionamiento de la Persistencia

### Flujo de Carga (Inicio del Programa)

```
┌─ Ejecución de main.py
│
├─ ArchivoServicio intenta abrir datos/productos.json
│
├─ Si el archivo NO existe
│  └─ Retorna lista vacía (primer inicio normal)
│
├─ Si el archivo EXISTE
│  ├─ json.load() recupera la estructura JSON
│  ├─ Valida que sea una lista
│  └─ Para cada registro:
│     ├─ Extrae campos obligatorios
│     ├─ Valida integridad de datos
│     ├─ Reconstruye objeto Producto o Bebida
│     └─ Lo agrega a la colección
│
└─ Restaurante recibe productos cargados y opera normalmente
```

### Flujo de Guardado (Después de Registrar/Actualizar/Eliminar)

```
┌─ Usuario realiza operación (registrar, actualizar, eliminar)
│
├─ Restaurante modifica su colección en memoria
│  ├─ Valida datos
│  ├─ Aplica cambios
│  └─ Retorna resultado de éxito/fracaso
│
├─ main.py verifica que operación fue exitosa
│
├─ main.py solicita a ArchivoServicio guardar la colección
│
├─ ArchivoServicio:
│  ├─ Convierte cada Producto a diccionario con a_diccionario()
│  ├─ Crea directorio datos/ si no existe
│  ├─ Abre datos/productos.json en modo escritura (UTF-8)
│  ├─ Escribe JSON formateado con json.dump()
│  └─ Cierra el archivo
│
└─ Usuario ve confirmación de guardado
```

### Estructura del Archivo `datos/productos.json`

```json
[
  {
    "tipo": "Producto",
    "codigo": "P001",
    "nombre": "Pizza Margarita",
    "categoria": "Pizzas",
    "precio": 12.50
  },
  {
    "tipo": "Bebida",
    "codigo": "B001",
    "nombre": "Coca Cola",
    "categoria": "Refrescos",
    "precio": 2.50,
    "tamano": "500ml",
    "envase": "botella"
  }
]
```

**Campo `tipo`:** Identifica si es "Producto" o "Bebida" para reconstruir correctamente

---

## Manejo de Excepciones

### FileNotFoundError
```
Situación: datos/productos.json no existe
Acción: Se inicializa con lista vacía, permite primer uso normal
Mensaje: "Archivo ... no encontrado. Iniciando con colección vacía."
```

### json.JSONDecodeError
```
Situación: Archivo existe pero contiene JSON inválido
Acción: Se informa del error y se inicia con colección vacía
Mensaje: "Error: El archivo ... no contiene JSON válido."
```

### PermissionError
```
Situación: Lectura o escritura sin permisos suficientes
Acción: Se aborta la operación de persistencia con mensaje informativo
Mensaje: "Error: No tiene permisos para leer/escribir ..."
```

### KeyError / ValueError
```
Situación: Registro incompleto o con datos inválidos en JSON
Acción: Se omite el registro problemático y continúa con los demás
Mensaje: "Advertencia: Registro #{idx} incompleto o inválido. Se omitirá."
```

---

## Instrucciones para Ejecutar

### Requisitos
- Python 3.8 o superior
- Módulos estándar únicamente (json, os)
- No requiere instalación de dependencias externas

### Ejecución

**Opción 1: Desde terminal en Windows PowerShell**
```powershell
cd "C:\Users\FERNANDO\Desktop\Nuevo repositorio\Parcial 2\Semana 10"
python restaurante_app/main.py
```

**Opción 2: Desde el directorio del proyecto**
```powershell
cd "C:\Users\FERNANDO\Desktop\Nuevo repositorio\Parcial 2\Semana 10\restaurante_app"
python main.py
```

### Menú Interactivo

Una vez ejecutado, aparecerá:
```
========================================
        SISTEMA DE RESTAURANTE
========================================
1. Registrar producto
2. Buscar producto
3. Actualizar producto
4. Eliminar producto
5. Listar productos
6. Registrar usuario
7. Eliminar usuario
8. Listar usuarios
9. Mostrar categorías
10. Salir

Seleccione una opción: _
```

---

## Comprobación de Persistencia

### Prueba Mínima Recomendada

1. **Ejecutar el programa**
   ```powershell
   python restaurante_app/main.py
   ```

2. **Registrar un producto**
   - Seleccionar opción 1
   - Ingresar datos (ej. código: P001, nombre: Pizza)
   - Confirmar que aparece "Producto registrado correctamente"
   - Confirmar que aparece "Cambios guardados en la base de datos"

3. **Verificar el archivo JSON**
   ```powershell
   Get-Content "C:\Users\FERNANDO\Desktop\Nuevo repositorio\Parcial 2\Semana 10\restaurante_app\datos\productos.json"
   ```
   - Debe mostrar el producto recién registrado en formato JSON

4. **Listar productos antes de cerrar**
   - Seleccionar opción 5
   - Confirmar que el producto aparece en la lista

5. **Cerrar completamente el programa**
   - Seleccionar opción 10
   - Proceso se detiene

6. **Ejecutar nuevamente el programa**
   ```powershell
   python restaurante_app/main.py
   ```
   - Debe mostrar mensaje de carga: "Se cargaron X producto(s) desde ..."

7. **Listar productos sin registrar ninguno nuevo**
   - Seleccionar opción 5
   - **CONFIRMACIÓN CRÍTICA:** El producto registrado anteriormente debe estar presente

8. **Realizar actualización**
   - Seleccionar opción 3
   - Buscar el producto registrado
   - Cambiar precio u otro atributo
   - Confirmar que se guardó

9. **Reiniciar nuevamente**
   - Seleccionar opción 10
   - Ejecutar el programa otra vez
   - Listar productos (opción 5)
   - **CONFIRMACIÓN:** El producto debe mantener los cambios realizados

### Casos de Prueba Adicionales

**Caso: Archivo JSON corrupto**
1. Editar `datos/productos.json` y escribir algo como: `{esto no es json valido`
2. Ejecutar el programa
3. Debe mostrar error controlado y continuar con lista vacía
4. Registrar un nuevo producto correctamente

**Caso: Permisos insuficientes** (Windows)
1. Click derecho en `datos/` → Propiedades → Seguridad
2. Remover permisos de escritura
3. Intentar registrar un producto
4. Debe mostrar error de permisos
5. Restaurar permisos y reintentar

**Caso: Primer inicio sin archivo**
1. Eliminar `datos/productos.json`
2. Ejecutar el programa
3. Debe mostrar mensaje de archivo no encontrado
4. Continuar normalmente con lista vacía

---

## Funcionalidades Conservadas de Semanas Anteriores

- ✅ **Registro de productos**: Crear nuevos productos de tipo genérico
- ✅ **Registro de bebidas**: Crear bebidas con campos adicionales (tamaño, envase)
- ✅ **Búsqueda**: Encontrar productos por código
- ✅ **Actualización**: Modificar datos de productos existentes
- ✅ **Eliminación**: Remover productos del sistema
- ✅ **Listado**: Ver todos los productos registrados
- ✅ **Categorías**: Visualizar categorías únicas de productos
- ✅ **Usuarios**: Registrar, listar y eliminar usuarios (sin persistencia)
- ✅ **Validaciones**: Mantener validaciones de datos antes de operaciones
- ✅ **Polimorfismo**: Trabajar con Producto y Bebida transparentemente

---

## Mejoras Implementadas en la Semana 10

| Aspecto | Cambio |
|--------|--------|
| **Persistencia** | Agregada para productos únicamente |
| **Archivo JSON** | Estructura clara con campo "tipo" para identificar subclases |
| **ArchivoServicio** | Nuevo servicio centralizado para I/O |
| **Método a_diccionario()** | Añadido a Producto y Bebida |
| **Excepciones** | Control específico de FileNotFoundError, JSONDecodeError, PermissionError, KeyError, ValueError |
| **Robustez** | El programa continúa incluso con registros incompletos en JSON |
| **Responsabilidades** | Claro separación entre persistencia (ArchivoServicio) y lógica (Restaurante) |

---

## Restricciones Respetadas

- ✅ No se reemplazó Producto por diccionarios
- ✅ No se utilizaron datos "quemados" en lugar de entrada del usuario
- ✅ No se limitó a solo crear el archivo JSON sin integrarlo
- ✅ No se realizó lectura/escritura desde múltiples puntos sin claridad
- ✅ No se utilizó `except: pass` para ocultar errores
- ✅ No se desarrollaron interfaces gráficas ni frameworks
- ✅ No se utilizaron bases de datos
- ✅ No se agregó persistencia obligatoria para usuarios
- ✅ No todo el código en un único archivo
- ✅ Se mantienen archivos `__init__.py` en paquetes
- ✅ Se mantiene la administración de productos dentro del servicio
- ✅ Se usan nombres descriptivos siguiendo convenciones Python
- ✅ Se aplican anotaciones de tipos en constructores y métodos

---

## Tecnologías Utilizadas

- **Lenguaje**: Python 3.8+
- **Módulos estándar**: `json`, `os`, `typing`, `re`
- **Paradigmas**: POO, separación de responsabilidades
- **Persistencia**: JSON

---

## Conclusión

La Semana 10 representa un paso importante en la evolución de Restaurante App: el sistema ahora puede **recordar datos entre ejecuciones**. Esto se logró mediante:

1. Una arquitectura clara donde **ArchivoServicio** maneja persistencia
2. Métodos de conversión que permiten ir de objetos a JSON y viceversa
3. Manejo robusto de excepciones sin sacrificar funcionalidad
4. Integración seamless con el código existente

El programa está listo para producción básica, permitiendo que un restaurante administre sus productos de forma confiable, con datos que persisten entre sesiones.

---

## Contacto y Entrega

**Repositorio GitHub:** [Enlace del repositorio]  
**Último actualizado:** 2024  
**Estado:** ✅ Completado y probado

---

*Documentación desarrollada siguiendo los estándares de la Semana 10, Parcial 2.*

