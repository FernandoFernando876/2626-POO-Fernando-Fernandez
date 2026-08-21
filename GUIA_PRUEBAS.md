# Guía de Pruebas - Restaurante App Semana 10

## Resumen de Pruebas Realizadas

Este documento describe las pruebas que se realizaron para validar la persistencia de productos con JSON.

### ✅ Pruebas Unitarias Completadas

#### 1. Estructura Inicial
- ✓ Verificación de directorios (modelos, servicios, datos)
- ✓ Verificación de archivos necesarios
- ✓ Confirmación de archivos `__init__.py`

#### 2. Conversión a Diccionario
- ✓ Método `a_diccionario()` en Producto
- ✓ Método `a_diccionario()` en Bebida
- ✓ Campo "tipo" para identificación de subclases
- ✓ Inclusión de todos los campos en JSON

#### 3. Persistencia Básica
- ✓ Guardado de productos en JSON
- ✓ Carga de productos desde JSON
- ✓ Integridad de datos guardados y recuperados
- ✓ Formato JSON válido y legible

#### 4. Ciclo Completo (Simulación de Reinicio)
- ✓ Registrar productos → Guardar → Cerrar
- ✓ Reiniciar programa → Cargar → Verificar persistencia
- ✓ Actualizar productos → Guardar → Cerrar
- ✓ Reiniciar → Verificar cambios persistieron
- ✓ Eliminar productos → Guardar → Cerrar
- ✓ Reiniciar → Verificar eliminación persistió

#### 5. Manejo de Excepciones

**FileNotFoundError (Primer inicio)**
```
Resultado: ✓ Se inicia con colección vacía
Comportamiento: Sistema continúa normalmente
Mensaje: "Archivo ... no encontrado. Iniciando con colección vacía."
```

**json.JSONDecodeError (JSON inválido)**
```
Resultado: ✓ Se detecta el error
Comportamiento: Se inicia con colección vacía
Mensaje: "El archivo ... no contiene JSON válido."
```

**KeyError/ValueError (Registro incompleto)**
```
Resultado: ✓ Se omite el registro problemático
Comportamiento: Se carga el resto de registros válidos
Mensaje: "Advertencia: Registro #{idx} incompleto o inválido. Se omitirá."
```

**Precio inválido (≤ 0)**
```
Resultado: ✓ Se rechaza el producto
Comportamiento: Se omite y continúa con siguientes
```

**Estructura inválida (No es lista)**
```
Resultado: ✓ Se detecta el error
Comportamiento: Se retorna colección vacía
Mensaje: "El archivo debe contener una lista JSON..."
```

---

## Cómo Ejecutar las Pruebas

### Pruebas Unitarias
```bash
cd C:\Users\FERNANDO\Desktop\Nuevo repositorio\Parcial 2\Semana 10\restaurante_app
python test_excepciones.py
```

**Resultado esperado:** Todos los tests deberían mostrar ✅

### Prueba Interactiva Manual

#### Paso 1: Primer Inicio (Archivo Vacío)
```bash
python main.py
```
- Debería mostrar: "Se cargaron 0 producto(s)"
- Menú debe aparecer normalmente
- Seleccionar opción 5 (Listar) → "No hay productos"

#### Paso 2: Registrar Producto
```
Opción seleccionada: 1

Registro de producto:
Código: PIZZA01
Nombre: Pizza Margarita
Categoría: Pizzas
Precio: 12.50
```

**Verificación:**
- Mensaje: "Producto registrado correctamente."
- Mensaje: "Cambios guardados en la base de datos."

#### Paso 3: Verificar Archivo JSON
```bash
type "C:\Users\FERNANDO\Desktop\Nuevo repositorio\Parcial 2\Semana 10\restaurante_app\datos\productos.json"
```

**Contenido esperado:**
```json
[
  {
    "tipo": "Producto",
    "codigo": "PIZZA01",
    "nombre": "Pizza Margarita",
    "categoria": "Pizzas",
    "precio": 12.5
  }
]
```

#### Paso 4: Registrar Más Productos
Repetir paso 2-3 con:
- Producto 2: PIZZA02, Pizza Hawaiana, Pizzas, 13.50
- Bebida: COCA01, Coca Cola, Refrescos, 2.50, 500ml, botella

#### Paso 5: Listar Productos
```
Opción seleccionada: 5

Listado de productos:
1. Código: PIZZA01 | Nombre: Pizza Margarita | Categoría: Pizzas | Precio: 12.50
2. Código: PIZZA02 | Nombre: Pizza Hawaiana | Categoría: Pizzas | Precio: 13.50
3. Código: COCA01 | Nombre: Coca Cola | Categoría: Refrescos | Precio: 2.50 | Tamaño: 500ml | Envase: botella
```

#### Paso 6: Buscar Producto
```
Opción seleccionada: 2
Código del producto a buscar: PIZZA01

Resultado:
Producto encontrado:
Código: PIZZA01 | Nombre: Pizza Margarita | Categoría: Pizzas | Precio: 12.50
```

#### Paso 7: Actualizar Producto
```
Opción seleccionada: 3
Código del producto a actualizar: PIZZA01
Nuevo nombre [Pizza Margarita]: 
Nueva categoría [Pizzas]: 
Nuevo precio [12.50]: 15.00

Resultado:
Producto actualizado correctamente.
Cambios guardados en la base de datos.
```

#### Paso 8: Cerrar Programa
```
Opción seleccionada: 10
Saliendo... ¡hasta luego!
```

#### Paso 9: Reiniciar Programa
```bash
python main.py
```

**Verificación crítica:**
- Mensaje: "Se cargaron 3 producto(s) desde ..."
- El precio de PIZZA01 debe ser 15.00 (NO 12.50)

#### Paso 10: Listar para Confirmar Persistencia
```
Opción seleccionada: 5

Debe mostrar:
1. Código: PIZZA01 | Nombre: Pizza Margarita | Categoría: Pizzas | Precio: 15.00 ← Cambio persistió
2. Código: PIZZA02 | Nombre: Pizza Hawaiana | Categoría: Pizzas | Precio: 13.50
3. Código: COCA01 | Nombre: Coca Cola | ... | Precio: 2.50
```

#### Paso 11: Eliminar Producto
```
Opción seleccionada: 4
Código del producto a eliminar: PIZZA02
Confirma eliminación? (s/n): s

Resultado:
Producto eliminado correctamente.
Cambios guardados en la base de datos.
```

#### Paso 12: Listar y Confirmar Eliminación
```
Opción seleccionada: 5

Debe mostrar solo 2 productos (PIZZA02 no aparece)
```

#### Paso 13: Cerrar y Reiniciar Final
```bash
python main.py
```

**Verificación final:**
- Debe cargar 2 productos
- PIZZA02 no debe estar presente
- PIZZA01 debe mantener precio de 15.00
- COCA01 debe estar intacta

---

## Prueba de Error: JSON Corrompido

### Paso 1: Corromper el archivo JSON
Editar `datos/productos.json` manualmente y cambiar:
```json
[
  { esto no es json válido }
]
```

### Paso 2: Ejecutar el programa
```bash
python main.py
```

**Resultado esperado:**
```
Inicializando sistema...
Error: El archivo datos/productos.json no contiene JSON válido. Detalles: ...
Iniciando con colección vacía. Revise manualmente el archivo JSON.
Se cargaron 0 producto(s) desde datos/productos.json.
Sistema listo.
```

### Paso 3: El menú debería funcionar normalmente
- Sistema no debería haberse detenido
- Debería permitir registrar nuevos productos
- El archivo se sobrescribirá con JSON válido al guardar

---

## Prueba de Error: Registro Incompleto

### Paso 1: Crear JSON con datos incompletos
Editar `datos/productos.json` manualmente:
```json
[
  {
    "tipo": "Producto",
    "codigo": "P001",
    "nombre": "Producto Sin Categoría"
    // Falta: "categoria" y "precio"
  },
  {
    "tipo": "Producto",
    "codigo": "P002",
    "nombre": "Producto Válido",
    "categoria": "Test",
    "precio": 10.00
  }
]
```

### Paso 2: Ejecutar el programa
```bash
python main.py
```

**Resultado esperado:**
```
Advertencia: Registro #1 incompleto o inválido. Se omitirá. Detalles: 'categoria'
Se cargaron 1 producto(s) desde datos/productos.json.
```

### Paso 3: Verificar que solo se cargó el válido
```
Opción 5 (Listar)
Listado de productos:
1. Código: P002 | Nombre: Producto Válido | ...
```

---

## Comparación: Antes y Después de la Persistencia

| Aspecto | Antes (Semana 9) | Después (Semana 10) |
|--------|-----------------|-------------------|
| **Almacenamiento** | Solo en memoria | Memoria + JSON |
| **Cierre del programa** | Datos se pierden | Datos se preservan |
| **Primer inicio** | Siempre vacío | Carga datos previos |
| **Archivo JSON** | No existe | Existe y se actualiza |
| **Recuperación de datos** | Manual por usuario | Automática al iniciar |

---

## Requisitos Cumplidos

✅ Sistema inicia correctamente sin archivo JSON  
✅ Productos se guardan en formato JSON  
✅ Productos se cargan correctamente al iniciar  
✅ Cambios en precios se persisten  
✅ Eliminaciones se persisten  
✅ JSON es legible (con indentación)  
✅ Se manejan excepciones específicas  
✅ Registros incompletos no detienen el programa  
✅ El menú funciona normalmente  
✅ Bebidas se guardan y cargan correctamente  
✅ Campo "tipo" identifica correctamente Producto vs Bebida  

---

## Comandos Útiles para Verificación

### Ver contenido del archivo JSON
```bash
Get-Content "datos/productos.json"
```

### Validar que el JSON es válido
```bash
python -c "import json; f=open('datos/productos.json'); json.load(f); print('✓ JSON válido')"
```

### Limpiar el archivo JSON (iniciar desde cero)
```bash
echo "[]" > datos/productos.json
```

### Ver el contenido con formato (en Python)
```bash
python -c "import json; f=open('datos/productos.json'); print(json.dumps(json.load(f), indent=2))"
```

---

## Conclusión

Todas las pruebas se han completado exitosamente. El sistema de persistencia funciona de forma robusta y confiable, manejando correctamente todos los casos de error esperados.

La aplicación está lista para producción básica.

