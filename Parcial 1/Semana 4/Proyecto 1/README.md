# Sistema de Gestión de Restaurante

## Información del Estudiante
**Nombre:** Robert Fernando Fernández Llori

---

## Descripción del Sistema

Este proyecto implementa un **Sistema Básico de Gestión de Restaurante** utilizando **Programación Orientada a Objetos (POO)** en Python. El sistema gestiona de forma modular y estructurada los elementos fundamentales de un restaurante: productos (platos y bebidas) y clientes.

### Objetivo
Demostrar la comprensión de cómo:
- Organizar un proyecto en módulos separados
- Separar responsabilidades entre clases
- Comunicar archivos mediante importaciones correctas
- Aplicar principios de POO (encapsulación, reutilización, abstracción)

---

## Estructura del Proyecto

```
Restaurante_App/
├── modelos/
│   ├── producto.py       # Clase que representa un producto del restaurante
│   └── cliente.py        # Clase que representa un cliente del restaurante
├── servicios/
│   └── restaurante.py    # Clase que gestiona la operación del restaurante
└── main.py               # Punto de entrada del programa
```

### Descripción de Módulos

#### 📦 **modelos/producto.py**
Define la clase `Producto` que representa un plato o bebida disponible en el restaurante.

**Atributos:**
- `id`: Identificador único del producto
- `nombre`: Nombre del producto
- `descripcion`: Descripción breve del producto
- `precio`: Precio del producto
- `disponible`: Estado de disponibilidad (booleano)

**Métodos principales:**
- `__init__()`: Inicializa un nuevo producto
- `__str__()`: Representación textual del producto
- `cambiar_disponibilidad()`: Alterna el estado de disponibilidad
- `obtener_informacion()`: Retorna información detallada en diccionario

---

#### 👤 **modelos/cliente.py**
Define la clase `Cliente` que representa a una persona que realiza pedidos.

**Atributos:**
- `id`: Identificador único del cliente
- `nombre`: Nombre completo del cliente
- `email`: Correo electrónico
- `telefono`: Número de teléfono
- `activo`: Estado del cliente (booleano)
- `pedidos_realizados`: Contador de pedidos

**Métodos principales:**
- `__init__()`: Inicializa un nuevo cliente
- `__str__()`: Representación textual del cliente
- `desactivar_cliente()` / `activar_cliente()`: Gestiona el estado
- `registrar_pedido()`: Incrementa el contador de pedidos
- `obtener_informacion()`: Retorna información detallada

---

#### 🏪 **servicios/restaurante.py**
Define la clase `Restaurante` que actúa como servicio principal y gestor del sistema.

**Atributos:**
- `nombre`: Nombre del restaurante
- `productos`: Lista de productos disponibles
- `clientes`: Lista de clientes registrados

**Métodos principales:**
- **Gestión de Productos:**
  - `agregar_producto()`: Añade un nuevo producto
  - `obtener_producto()`: Busca un producto por ID
  - `listar_productos()`: Retorna productos disponibles
  - `eliminar_producto()`: Elimina un producto
  
- **Gestión de Clientes:**
  - `agregar_cliente()`: Añade un nuevo cliente
  - `obtener_cliente()`: Busca un cliente por ID
  - `listar_clientes()`: Retorna clientes activos
  - `eliminar_cliente()`: Elimina un cliente
  
- **Información:**
  - `obtener_estadisticas()`: Retorna datos estadísticos del restaurante
  - `mostrar_informacion()`: Muestra un reporte completo en consola

---

#### 🚀 **main.py**
Punto de entrada principal del programa que demuestra el funcionamiento del sistema.

**Demostración incluye:**
1. Creación del restaurante
2. Adición de 5 productos (pastas, pizzas, ensaladas, carnes y bebidas)
3. Registro de 4 clientes
4. Simulación de pedidos
5. Cambio de disponibilidad de productos
6. Desactivación de clientes
7. Visualización completa de la información del restaurante

---

## Ejecución del Programa

Para ejecutar el programa:

```bash
# Cambiar al directorio del proyecto
cd Restaurante_App/

# Ejecutar el programa principal
python main.py
```

**Requisitos:**
- Python 3.x instalado
- Sin dependencias externas requeridas

---

## Características Implementadas ✓

- ✅ Estructura modular en carpetas (modelos, servicios)
- ✅ Dos clases en modelos (Producto, Cliente)
- ✅ Una clase en servicios (Restaurante)
- ✅ Constructor `__init__()` en todas las clases principales
- ✅ Método especial `__str__()` para representación textual
- ✅ Importaciones correctas entre módulos
- ✅ Creación de objetos en main.py
- ✅ Adición de objetos al servicio principal
- ✅ Información organizada mostrada en consola
- ✅ Comentarios explicativos en el código
- ✅ Atributos y métodos pertinentes al contexto del restaurante

---

## Reflexión: Importancia de la Modularización y Separación de Responsabilidades

### ¿Por qué modularizar el software?

**1. Mantenibilidad**
La división clara del código en módulos independientes facilita la identificación y corrección de errores. Si existe un problema con la lógica de clientes, sabemos exactamente dónde buscar.

**2. Escalabilidad**
Un proyecto modular permite agregar nuevas funcionalidades sin afectar el código existente. Por ejemplo, podríamos agregar una nueva clase `Pedido` en modelos sin modificar las clases existentes.

**3. Reutilización**
Las clases bien diseñadas pueden ser reutilizadas en otros proyectos. La clase `Producto` podría usarse en sistemas de inventario, catálogos, tiendas en línea, etc.

**4. Colaboración**
En equipos de desarrollo, diferentes programadores pueden trabajar simultáneamente en diferentes módulos sin conflictos. Un desarrollador en clientes, otro en productos, otro en servicios.

**5. Testabilidad**
El código modular es más fácil de probar. Podemos escribir pruebas unitarias específicas para cada clase sin necesidad de toda la aplicación.

### Separación de Responsabilidades

En este proyecto aplicamos el principio de **Single Responsibility Principle (SRP)**:

- **Producto**: Solo se encarga de representar la información y comportamiento de un producto
- **Cliente**: Solo gestiona la información y estado de un cliente
- **Restaurante**: Actúa como coordinador central que administra colecciones de productos y clientes

Esta separación evita que una clase tenga múltiples razones para cambiar, haciendo el código más robusto y flexible.

### Beneficios Demostrados

En nuestro sistema:
- Fácil de extender (agregar nuevas métodos o clases)
- Fácil de entender (responsabilidades claras)
- Fácil de mantener (cambios localizados)
- Fácil de probar (componentes independientes)

---

## Notas de Desarrollo

- Este proyecto no utiliza funcionalidades avanzadas como herencia o polimorfismo, manteniéndose dentro del alcance de conceptos básicos de POO.
- El enfoque está en la organización y estructuración modular, no en la complejidad de la lógica.
- El código es ilustrativo y puede ser extendido con características adicionales como persistencia en base de datos, interfaz gráfica, validación de datos, etc.

---

## Licencia

Este proyecto fue desarrollado como actividad educativa en el curso de Programación Orientada a Objetos.

---

**Fecha de entrega:** Junio 2026

