# 🏪 Sistema de Restaurante - Programación Orientada a Objetos

## 📋 Descripción del Proyecto

Este proyecto implementa un sistema de gestión de restaurante utilizando **Programación Orientada a Objetos (POO)** en Python. El sistema permite registrar, listar y buscar **productos** y **clientes** mediante un menú interactivo ejecutado desde la consola.

El objetivo educativo es demostrar la comprensión de conceptos fundamentales de POO:
- ✅ Constructores tradicionales (`__init__`)
- ✅ Decoradores `@property` y `@setter` para encapsulación
- ✅ Decorador `@dataclass` para definición simplificada de clases
- ✅ Arquitectura modular por capas (modelos y servicios)
- ✅ Creación de objetos desde datos ingresados por usuario
- ✅ Almacenamiento y gestión de objetos en listas

---

## 🏗️ Estructura del Proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py          # Inicializador del módulo modelos
│   ├── producto.py          # Clase Producto (constructor + @property + @setter)
│   └── cliente.py           # Clase Cliente (@dataclass)
├── servicios/
│   ├── __init__.py          # Inicializador del módulo servicios
│   └── restaurante.py       # Clase Restaurante (servicio de gestión)
├── main.py                  # Punto de entrada y menú interactivo
└── README.md                # Este archivo
```

---

## 📦 Componentes Principales

### 1. **modelos/producto.py** - Clase Producto

Implementa un producto del restaurante con:

- **Constructor tradicional (`__init__`)**: Inicializa los atributos privados
- **Atributos privados**: `_nombre`, `_categoria`, `_precio`, `_disponible`
- **Decoradores `@property`**: Permite acceso controlado a los atributos
- **Decoradores `@setter`**: Valida datos antes de modificar atributos

**Validaciones implementadas:**
- ✅ El nombre no puede estar vacío
- ✅ La categoría no puede estar vacía
- ✅ El precio debe ser mayor que cero

**Ejemplo de uso:**
```python
# Creación de objeto mediante constructor
producto = Producto(
    nombre="Hamburguesa",
    categoria="Platillo",
    precio=8.50
)

# Acceso a atributos mediante @property
print(producto.nombre)  # "Hamburguesa"

# Modificación mediante @setter (con validación)
producto.precio = 9.50  # ✅ Válido
producto.precio = -5    # ❌ Genera ValueError
```

---

### 2. **modelos/cliente.py** - Clase Cliente

Implementa un cliente del restaurante utilizando **@dataclass**:

- **Decorador `@dataclass`**: Genera automáticamente `__init__`, `__repr__`, `__eq__`, etc.
- **Atributos**: `id_cliente`, `nombre`, `correo`

**Ejemplo de uso:**
```python
# Creación simplificada con @dataclass
cliente = Cliente(
    id_cliente="C001",
    nombre="Juan García",
    correo="juan@email.com"
)

# __init__ es generado automáticamente por @dataclass
# __repr__ también está disponible automáticamente
print(cliente)  # Cliente(id_cliente='C001', nombre='Juan García', correo='juan@email.com')
```

---

### 3. **servicios/restaurante.py** - Clase Restaurante

Clase de servicio que administra productos y clientes:

**Métodos para Productos:**
- `registrar_producto(producto)`: Agrega un nuevo producto
- `listar_productos()`: Muestra todos los productos
- `buscar_producto_por_nombre(nombre)`: Busca por nombre
- `buscar_producto_por_categoria(categoria)`: Busca por categoría

**Métodos para Clientes:**
- `registrar_cliente(cliente)`: Agrega un nuevo cliente
- `listar_clientes()`: Muestra todos los clientes
- `buscar_cliente_por_nombre(nombre)`: Busca por nombre
- `buscar_cliente_por_id(id_cliente)`: Busca por ID

**Métodos Generales:**
- `mostrar_resumen()`: Muestra estadísticas del restaurante

---

### 4. **main.py** - Menú Interactivo

Punto de entrada del programa con:

- Menú interactivo ejecutable desde consola
- Funciones para cada opción del menú
- Carga de datos de ejemplo (didácticos)
- Flujo: `input() → constructor → objeto → registro → búsqueda`

---

## 🚀 Cómo Ejecutar el Proyecto

### Requisitos
- Python 3.7 o superior
- Sin dependencias externas (utiliza solo la librería estándar)

### Pasos para ejecutar

1. **Abrir terminal en la carpeta del proyecto:**
   ```bash
   cd C:\Users\FERNANDO\Desktop\Nuevo\ repositorio\Parcial\ 1\Semana\ 7\restaurante_app
   ```

2. **Ejecutar el programa:**
   ```bash
   python main.py
   ```

3. **Ver el menú interactivo:**
   ```
   ==================================================
           🏪 SISTEMA DE RESTAURANTE
   ==================================================
   1. Registrar producto
   2. Listar productos
   3. Buscar producto
   ─────────────────────────────────────────────────
   4. Registrar cliente
   5. Listar clientes
   6. Buscar cliente
   ─────────────────────────────────────────────────
   0. Ver resumen del restaurante
   7. Salir
   ==================================================
   ```

---

## 📚 Ejemplo de Flujo de Ejecución

### Flujo: Registrar un Producto

```
Usuario selecciona opción "1"
        ↓
Se solicita: nombre, categoría, precio
        ↓
input() obtiene los datos del usuario
        ↓
Constructor __init__ crea objeto Producto:
  - Valida nombre (no vacío)
  - Valida categoría (no vacío)
  - Valida precio (> 0)
        ↓
Objeto Producto es registrado en Restaurante
        ↓
Se muestra confirmación al usuario
```

### Flujo: Listar Productos

```
Usuario selecciona opción "2"
        ↓
Se llama a restaurante.listar_productos()
        ↓
Se itera sobre la lista de productos almacenados
        ↓
Se muestra cada producto con formato legible
```

### Flujo: Buscar Producto

```
Usuario selecciona opción "3"
        ↓
Se solicita: nombre o categoría
        ↓
Se busca en la lista de productos
        ↓
Se muestran los resultados encontrados
```

---

## 🎓 Conceptos de POO Implementados

### 1. **Encapsulación mediante @property y @setter**

```python
# Atributos privados (convención: _nombre)
self._precio = None

# Acceso controlado mediante @property
@property
def precio(self):
    return self._precio

# Modificación con validación mediante @setter
@precio.setter
def precio(self, valor):
    if float(valor) <= 0:
        raise ValueError("El precio debe ser mayor que cero.")
    self._precio = float(valor)
```

### 2. **Uso de @dataclass**

```python
from dataclasses import dataclass

@dataclass
class Cliente:
    id_cliente: str
    nombre: str
    correo: str
    # __init__, __repr__, __eq__ son generados automáticamente
```

### 3. **Arquitectura por Capas**

- **Capa de Modelos**: Define entidades (Producto, Cliente)
- **Capa de Servicios**: Administra lógica de negocio (Restaurante)
- **Capa de Presentación**: Interfaz con usuario (main.py)

### 4. **Creación de Objetos desde Entrada de Usuario**

```python
# Datos ingresados por usuario
nombre = input("Ingrese nombre: ")
precio = input("Ingrese precio: ")

# Creación de objeto mediante constructor
nuevo_producto = Producto(nombre=nombre, precio=float(precio))

# Registro en servicio
restaurante.registrar_producto(nuevo_producto)
```

---

## 📊 Datos de Ejemplo Cargados

El sistema inicia con datos didácticos pre-cargados:

**Productos:**
- Hamburguesa Clásica ($8.50)
- Pizza Margherita ($12.00)
- Ensalada César ($9.99)
- Coca-Cola ($2.50)
- Jugo Natural ($3.50)
- Flan Casero ($4.00)
- Brownie Chocolatero ($5.50)

**Clientes:**
- C001: Juan García (juan.garcia@email.com)
- C002: María López (maria.lopez@email.com)
- C003: Carlos Rodríguez (carlos.rodriguez@email.com)
- C004: Ana Martínez (ana.martinez@email.com)

Estos datos permiten probar inmediatamente las funcionalidades de búsqueda y listado.

---

## ✅ Requisitos Cumplidos

- ✅ Estructura modular en carpetas (`modelos/`, `servicios/`)
- ✅ Clase `Producto` con constructor tradicional `__init__`
- ✅ Decoradores `@property` y `@setter` en Producto
- ✅ Validaciones de atributos en Producto
- ✅ Clase `Cliente` con decorador `@dataclass`
- ✅ Clase `Restaurante` que administra productos y clientes
- ✅ Métodos para registrar, listar y buscar
- ✅ Menú interactivo en `main.py`
- ✅ Creación de objetos desde entrada de usuario (input)
- ✅ Ausencia de objetos quemados directamente en código
- ✅ Uso de identificadores descriptivos y convenciones Python
- ✅ Comentarios explicativos en el código
- ✅ Datos de ejemplo para fines didácticos
- ✅ Sin dependencias externas
- ✅ Sin bases de datos ni archivos externos
- ✅ Sin interfaces gráficas

---

## 🔧 Posibles Mejoras Futuras

- Persistencia de datos en archivos JSON o base de datos
- Edición y eliminación de productos/clientes
- Sistema de órdenes o reservas
- Validación de correos electrónicos
- Interfaz gráfica con tkinter
- API REST con Flask o FastAPI

---

## 📝 Autor

Estudiante de Programación Orientada a Objetos - Semana 7

---

## 📄 Licencia

Este proyecto es de naturaleza educativa.

