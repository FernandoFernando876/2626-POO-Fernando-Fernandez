# Sistema de Gestión de Restaurante - Semana 5

## 📋 Descripción del Proyecto

Sistema básico de gestión de restaurante desarrollado con **Programación Orientada a Objetos (POO)** en Python. El objetivo es demostrar la aplicación de conceptos fundamentales de POO mediante una estructura modular y organizada.

---

## 🏗️ Estructura del Proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py        # Clase Producto
│   └── cliente.py         # Clase Cliente
├── servicios/
│   ├── __init__.py
│   └── restaurante.py     # Clase Restaurante (gestión)
└── main.py                # Punto de arranque del programa
```

---

## 🎯 Clases Implementadas

### 1. **Clase Producto** (`modelos/producto.py`)

Representa un plato, bebida o servicio disponible en el restaurante.

**Atributos:**
- `id_producto` (int): Identificador único
- `nombre` (str): Nombre del producto
- `descripcion` (str): Descripción detallada
- `precio` (float): Precio en unidades monetarias
- `disponible` (bool): Estado de disponibilidad

**Métodos:**
- `obtener_disponibilidad()`: Retorna el estado del producto
- `cambiar_disponibilidad(disponible)`: Modifica la disponibilidad
- `obtener_informacion_precio()`: Formatea el precio
- `__str__()`: Representación en texto del producto

---

### 2. **Clase Cliente** (`modelos/cliente.py`)

Representa un cliente registrado en el sistema del restaurante.

**Atributos:**
- `id_cliente` (int): Identificador único
- `nombre_completo` (str): Nombre completo del cliente
- `email` (str): Correo electrónico
- `telefono` (str): Número de teléfono
- `activo` (bool): Estado activo/inactivo

**Métodos:**
- `obtener_estado()`: Retorna el estado del cliente
- `cambiar_estado(activo)`: Modifica el estado del cliente
- `obtener_datos_contacto()`: Retorna datos de contacto
- `__str__()`: Representación en texto del cliente

---

### 3. **Clase Restaurante** (`servicios/restaurante.py`)

Administra listas de productos y clientes del restaurante.

**Atributos:**
- `nombre_restaurante` (str): Nombre del restaurante
- `lista_productos` (List[Producto]): Lista de productos
- `lista_clientes` (List[Cliente]): Lista de clientes

**Métodos:**

**Gestión de Productos:**
- `agregar_producto(producto)`: Agrega un producto
- `obtener_total_productos()`: Retorna cantidad de productos
- `obtener_productos_disponibles()`: Lista productos disponibles
- `mostrar_productos()`: Muestra todos los productos

**Gestión de Clientes:**
- `agregar_cliente(cliente)`: Agrega un cliente
- `obtener_total_clientes()`: Retorna cantidad de clientes
- `obtener_clientes_activos()`: Lista clientes activos
- `mostrar_clientes()`: Muestra todos los clientes

**Información General:**
- `mostrar_resumen_general()`: Resumen de estadísticas
- `mostrar_informacion_completa()`: Muestra toda la información

---

## ✨ Características Implementadas

✅ **Identificadores descriptivos**: Nombres claros y significativos en clases, métodos y variables
✅ **Convenciones de nombres**: PascalCase para clases, snake_case para variables y métodos
✅ **Tipos de datos**: str, int, float, bool y List
✅ **Anotaciones de tipo**: Especificadas en atributos y parámetros
✅ **Constructor `__init__()`**: En todas las clases principales
✅ **Método `__str__()`**: Para representación en texto
✅ **Importaciones correctas**: Entre módulos del proyecto
✅ **Listas como tipo compuesto**: Para almacenar productos y clientes
✅ **Métodos de gestión**: Para agregar, modificar y consultar información
✅ **Comentarios explicativos**: Documentación en el código

---

## 🚀 Cómo Ejecutar el Programa

### Desde el directorio del proyecto:

```bash
# Navegar al directorio
cd "Parcial 1/Semana 5/restaurante_app"

# Ejecutar el programa
python main.py
```

### Requisitos:
- Python 3.x instalado
- Sin dependencias externas requeridas

---

## 📊 Ejemplo de Ejecución

El programa realiza las siguientes operaciones:

1. Crea una instancia del restaurante
2. Crea 4 objetos de tipo `Producto`
3. Crea 4 objetos de tipo `Cliente`
4. Agrega productos y clientes al restaurante
5. Muestra la información completa del restaurante
6. Realiza demostraciones de funcionalidades (cambios de estado)
7. Muestra productos disponibles y clientes activos

**Salida esperada:** Se muestran tablas formateadas con información organizada de productos y clientes.

---

## 🎓 Conceptos POO Demostratos

- ✅ **Encapsulación**: Atributos y métodos encapsulados en clases
- ✅ **Abstracción**: Comportamiento ocultado en métodos
- ✅ **Modularización**: Organización en carpetas y módulos
- ✅ **Herencia**: Estructura para futuras extensiones
- ✅ **Responsabilidad Única**: Cada clase con propósito específico

---

## 📝 Notas Importantes

- El código sigue la **PEP 8** de Python
- Los comentarios están en español para mayor claridad
- La estructura es escalable para futuras mejoras
- No se implementaron interfaces gráficas ni menús interactivos
- El enfoque es en claridad y buenas prácticas de código

---

**Fecha de Creación:** Junio 2026  
**Autor:** Robert Fernando Fernández Llori  
**Curso:** Programación Orientada a Objetos (POO)

