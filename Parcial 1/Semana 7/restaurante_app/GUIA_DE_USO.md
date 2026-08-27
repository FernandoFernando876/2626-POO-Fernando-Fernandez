# 📖 GUÍA DE USO - Sistema de Restaurante

## 🎯 Objetivo de Aprendizaje

Este proyecto demuestra conceptos fundamentales de **Programación Orientada a Objetos (POO)**:

```
┌─────────────────────────────────────────────────────────┐
│          CONCEPTOS POO DEMOSTRADOS                      │
├─────────────────────────────────────────────────────────┤
│ ✅ Constructores tradicionales (__init__)              │
│ ✅ Encapsulación con @property y @setter               │
│ ✅ Validación de datos en atributos                    │
│ ✅ Decorador @dataclass                                │
│ ✅ Arquitectura por capas (MVC simplificado)           │
│ ✅ Creación de objetos desde entrada de usuario        │
│ ✅ Almacenamiento en listas de servicio                │
│ ✅ Búsqueda y recuperación de datos                    │
└─────────────────────────────────────────────────────────┘
```

---

## 🚀 CÓMO EJECUTAR

### Opción 1: Ejecutar desde PowerShell

```powershell
cd "C:\Users\FERNANDO\Desktop\Nuevo repositorio\Parcial 1\Semana 7\restaurante_app"
python main.py
```

### Opción 2: Ejecutar desde VSCode

1. Abrir la carpeta en VSCode
2. Abrir terminal integrada (Ctrl + `)
3. Ejecutar: `python main.py`

### Opción 3: Desde el Explorador de Archivos

1. Navegar a la carpeta `restaurante_app`
2. Hacer clic derecho en `main.py`
3. Seleccionar "Abrir con" → "Python"

---

## 📱 MENÚ INTERACTIVO

Al ejecutar el programa, verás este menú:

```
==================================================
        🏪 SISTEMA DE RESTAURANTE
==================================================
1. Registrar producto
2. Listar productos
3. Buscar producto
──────────────────────────────────────────────────
4. Registrar cliente
5. Listar clientes
6. Buscar cliente
──────────────────────────────────────────────────
0. Ver resumen del restaurante
7. Salir
==================================================
```

---

## 📚 EJEMPLOS DE USO

### Ejemplo 1: Listar Productos

```
Seleccione una opción: 2

==================================================
📦 LISTADO DE PRODUCTOS (7 registrados)
==================================================
1. ✅ Hamburguesa Clásica (Platillo) - $8.50
2. ✅ Pizza Margherita (Platillo) - $12.00
3. ✅ Ensalada César (Platillo) - $9.99
4. ✅ Coca-Cola (Bebida) - $2.50
5. ✅ Jugo Natural (Bebida) - $3.50
6. ✅ Flan Casero (Postre) - $4.00
7. ✅ Brownie Chocolatero (Postre) - $5.50
==================================================
```

### Ejemplo 2: Buscar Producto por Nombre

```
Seleccione una opción: 3

==================================================
🔍 BUSCAR PRODUCTO
==================================================
1. Buscar por nombre
2. Buscar por categoría
3. Volver

Seleccione una opción: 1
Ingrese el nombre del producto a buscar: Pizza

==================================================
🔍 BÚSQUEDA DE PRODUCTOS - 'Pizza'
==================================================
1. ✅ Pizza Margherita (Platillo) - $12.00
==================================================
```

### Ejemplo 3: Listar Clientes

```
Seleccione una opción: 5

==================================================
👥 LISTADO DE CLIENTES (4 registrados)
==================================================
1. 👤 Juan García (ID: C001) - juan.garcia@email.com
2. 👤 María López (ID: C002) - maria.lopez@email.com
3. 👤 Carlos Rodríguez (ID: C003) - carlos.rodriguez@email.com
4. 👤 Ana Martínez (ID: C004) - ana.martinez@email.com
==================================================
```

### Ejemplo 4: Ver Resumen

```
Seleccione una opción: 0

==================================================
🏪 RESUMEN DEL RESTAURANTE - La Buena Mesa
==================================================
📦 Productos registrados: 7
👥 Clientes registrados:  4
==================================================
```

---

## 💾 FLUJO DE CREACIÓN DE OBJETOS

### Cuando se registra un Producto:

```
1. Usuario selecciona opción "1" (Registrar producto)
                    ↓
2. Sistema solicita datos: nombre, categoría, precio
                    ↓
3. Usuario ingresa datos mediante input()
                    ↓
4. CONSTRUCTOR __init__ valida y crea objeto Producto:
   - Valida que nombre no esté vacío (mediante @setter)
   - Valida que categoría no esté vacía (mediante @setter)
   - Valida que precio sea > 0 (mediante @setter)
                    ↓
5. Objeto Producto es almacenado en lista de Restaurante
                    ↓
6. Sistema muestra confirmación con ✅
```

### Cuando se registra un Cliente:

```
1. Usuario selecciona opción "4" (Registrar cliente)
                    ↓
2. Sistema solicita datos: ID, nombre, correo
                    ↓
3. Usuario ingresa datos mediante input()
                    ↓
4. DECORADOR @dataclass crea automáticamente el objeto Cliente:
   - Genera __init__() automáticamente
   - Genera __repr__() automáticamente
   - Genera __eq__() automáticamente
                    ↓
5. Objeto Cliente es almacenado en lista de Restaurante
                    ↓
6. Sistema muestra confirmación con ✅
```

---

## 🔍 DEMOSTRACIÓN DE @PROPERTY Y @SETTER

Internamente, el sistema funciona así:

```python
# Cuando se crea un Producto:
nuevo_producto = Producto(
    nombre="Hamburguesa",      # ← Usa @setter para validar
    categoria="Platillo",       # ← Usa @setter para validar
    precio=8.50                 # ← Usa @setter para validar
)

# Cuando accedemos a los datos:
print(nuevo_producto.nombre)    # ← Usa @property para leer
print(nuevo_producto.precio)    # ← Usa @property para leer

# Si intentamos modificar con datos inválidos:
nuevo_producto.precio = -5      # ❌ ValueError (validado por @setter)
nuevo_producto.precio = 9.50    # ✅ Válido (autorizado por @setter)
```

---

## 🎓 COMPARACIÓN: Constructor vs @dataclass

### Clase Producto (Constructor Tradicional)

```python
class Producto:
    def __init__(self, nombre, categoria, precio, disponible=True):
        # Validación manual de cada atributo
        self._nombre = None
        self.nombre = nombre  # Usa @setter
        
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        if not valor or not str(valor).strip():
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = str(valor).strip()
```

**Ventajas:**
- Control granular sobre validación
- Encapsulación explícita
- Mayor flexibilidad

### Clase Cliente (@dataclass)

```python
from dataclasses import dataclass

@dataclass
class Cliente:
    id_cliente: str
    nombre: str
    correo: str
```

**Ventajas:**
- Menos código (boilerplate reducido)
- Generación automática de métodos
- Más legible y conciso

---

## ✅ CHECKLIST DE REQUISITOS CUMPLIDOS

### Estructura del Proyecto
- ✅ Carpeta `modelos/` con `__init__.py`
- ✅ Carpeta `servicios/` con `__init__.py`
- ✅ Archivo `main.py` como punto de entrada

### Clase Producto
- ✅ Constructor tradicional `__init__`
- ✅ Decoradores `@property` y `@setter`
- ✅ Atributos: nombre, categoría, precio, disponible
- ✅ Validación: nombre no vacío
- ✅ Validación: categoría no vacía
- ✅ Validación: precio > 0
- ✅ Método `mostrar_informacion()`

### Clase Cliente
- ✅ Decorador `@dataclass`
- ✅ Atributos: id_cliente, nombre, correo
- ✅ Método `mostrar_informacion()`

### Clase Restaurante
- ✅ Método `registrar_producto()`
- ✅ Método `listar_productos()`
- ✅ Método `buscar_producto_por_nombre()`
- ✅ Método `buscar_producto_por_categoria()`
- ✅ Método `registrar_cliente()`
- ✅ Método `listar_clientes()`
- ✅ Método `buscar_cliente_por_nombre()`
- ✅ Método `buscar_cliente_por_id()`

### Menú Interactivo
- ✅ 7 opciones principales
- ✅ Datos ingresados desde `input()`
- ✅ Creación de objetos desde entrada de usuario
- ✅ Registro en Restaurante
- ✅ Búsqueda y listado

### Datos de Ejemplo
- ✅ 7 productos pre-cargados
- ✅ 4 clientes pre-cargados
- ✅ Sistema cargado al iniciar (didáctico)

---

## 🧪 CASOS DE PRUEBA

### Prueba 1: Validación de Precio Negativo

```python
# En la función registrar_producto()
Ingrese el nombre: Café
Ingrese la categoría: Bebida
Ingrese el precio: -5

# Resultado esperado:
❌ Error: El precio debe ser mayor que cero.
```

### Prueba 2: Búsqueda sin Resultados

```
Seleccione una opción: 3
1
Ingrese el nombre del producto a buscar: Sushi

# Resultado esperado:
❌ No se encontraron productos con el nombre 'Sushi'.
```

### Prueba 3: Listado de Clientes Vacío

```
# Si eliminamos todos los clientes (no implementado en esta versión):
⚠️ No hay clientes registrados.
```

---

## 🎯 APRENDIZAJE ESPERADO

Después de ejecutar y explorar este sistema, deberías entender:

1. **Constructores**: Cómo inicializar objetos con validación
2. **@property y @setter**: Cómo controlar acceso a atributos
3. **@dataclass**: Cómo simplificar definición de clases
4. **Arquitectura por capas**: Separación entre modelos, servicios y presentación
5. **Flujo de datos**: Input → Objeto → Almacenamiento → Búsqueda
6. **Encapsulación**: Atributos privados (_) protegidos por métodos públicos
7. **Reutilización**: Un mismo objeto puede listarse y buscarse múltiples veces

---

## 🐛 SOLUCIÓN DE PROBLEMAS

### Error: "ModuleNotFoundError: No module named 'servicios'"

**Solución:** Asegúrate de estar ejecutando desde la carpeta correcta:
```powershell
cd "C:\Users\FERNANDO\Desktop\Nuevo repositorio\Parcial 1\Semana 7\restaurante_app"
python main.py
```

### Error: "No such file or directory"

**Solución:** Verifica que los archivos `__init__.py` existan en carpetas `modelos/` y `servicios/`

### El programa no acepta entrada

**Solución:** Algunos IDE requieren que ejecutes desde terminal externa. Usa:
```powershell
python main.py
```
En lugar de hacer clic en "Run".

---

## 📝 PRÓXIMOS PASOS

Puedes mejorar este sistema con:

1. **Editar productos/clientes**: Agregar opción de modificar datos
2. **Eliminar registros**: Permitir borrar productos y clientes
3. **Persistencia**: Guardar datos en archivos JSON
4. **Órdenes**: Sistema de órdenes para clientes
5. **Validación de email**: Verificar formato de correo
6. **Reportes**: Generar resúmenes estadísticos

---

## 📚 REFERENCIAS

- [Python @property](https://docs.python.org/3/library/functions.html#property)
- [Python @dataclass](https://docs.python.org/3/library/dataclasses.html)
- [Encapsulación en POO](https://en.wikipedia.org/wiki/Encapsulation_(computer_programming))
- [Arquitectura por capas](https://en.wikipedia.org/wiki/Multitier_architecture)

---

**¡Felicidades! 🎉 Ya comprendes los conceptos fundamentales de POO en Python.**

