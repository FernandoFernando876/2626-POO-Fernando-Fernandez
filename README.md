# Sistema de Gestión de Restaurante

**Estudiante:** Robert Fernando Fernández Llori

## Descripción del Sistema

Este proyecto implementa un sistema de gestión de restaurante que demuestra la aplicación práctica de los principios SOLID (Single Responsibility, Open/Closed, Liskov Substitution Principle). El sistema permite registrar productos, bebidas y clientes mediante un menú interactivo ejecutado desde consola.

El proyecto fue desarrollado como parte de la **Semana 8 - Parcial 1** del curso de Programación Orientada a Objetos en Python, utilizando los conceptos de herencia, polimorfismo y encapsulamiento para mantener un código limpio, mantenible y escalable.

## Estructura del Proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py         # Clase base Producto
│   ├── bebida.py           # Clase Bebida (hereda de Producto)
│   └── cliente.py          # Clase Cliente
├── servicios/
│   ├── __init__.py
│   └── restaurante.py      # Servicio que administra colecciones
└── main.py                 # Menú interactivo principal
```

## Responsabilidad de Cada Clase

### `modelos/producto.py` — Clase `Producto`
**Responsabilidad única:** Representar un producto genérico del restaurante con sus datos básicos.

- **Atributos:**
  - `codigo` (str): Identificador único del producto
  - `nombre` (str): Nombre descriptivo
  - `categoria` (str): Categoría o tipo de producto
  - `precio` (float): Precio en unidades monetarias

- **Métodos:**
  - `__init__()`: Inicializa un producto
  - `mostrar_informacion()`: Devuelve una representación textual del producto

**Principio SOLID aplicado:** Single Responsibility (S) — Solo se encarga de representar datos de un producto y su presentación.

### `modelos/bebida.py` — Clase `Bebida`
**Responsabilidad única:** Extender la funcionalidad de Producto para bebidas específicas.

- **Herencia:** Extiende `Producto`
- **Atributos adicionales:**
  - `tamano` (str): Tamaño de la bebida (ej. "500ml", "1L")
  - `envase` (str): Tipo de envase (ej. "botella", "lata", "vaso")

- **Métodos:**
  - `__init__()`: Inicializa una bebida (llama a `super().__init__()`)
  - `mostrar_informacion()`: Sobrescribe el método padre para incluir información específica

**Principio SOLID aplicado:** Single Responsibility (S) — Encargada únicamente de extender datos de bebidas sin alterar la lógica general.

### `modelos/cliente.py` — Clase `Cliente`
**Responsabilidad única:** Representar a un cliente registrado en el sistema.

- **Atributos:**
  - `identificacion` (str): ID única del cliente
  - `nombre` (str): Nombre completo
  - `correo` (str): Correo electrónico

- **Métodos:**
  - `__init__()`: Inicializa un cliente
  - `mostrar_informacion()`: Devuelve una representación textual del cliente

**Principio SOLID aplicado:** Single Responsibility (S) — Solo representa datos de cliente.

### `servicios/restaurante.py` — Clase `Restaurante`
**Responsabilidad única:** Administrar y orquestar el registro, validación y listado de productos y clientes.

- **Atributos privados:**
  - `_productos` (List[Producto]): Colección de productos y bebidas
  - `_clientes` (List[Cliente]): Colección de clientes

- **Métodos públicos:**
  - `registrar_producto(producto)`: Agrega un producto (válida duplicados)
  - `listar_productos()`: Devuelve información formateada de todos los productos
  - `registrar_cliente(cliente)`: Agrega un cliente (válida duplicados)
  - `listar_clientes()`: Devuelve información formateada de todos los clientes

- **Métodos privados:**
  - `_existe_codigo_producto(codigo)`: Valida códigos únicos
  - `_existe_identificacion_cliente(identificacion)`: Valida IDs únicas

**Principio SOLID aplicado:**
  - Single Responsibility (S): Solo administra las colecciones
  - Encapsulamiento: Los atributos `_productos` y `_clientes` son privados

### `main.py` — Punto de Entrada
**Responsabilidad única:** Interactuar con el usuario y llamar a los métodos del servicio `Restaurante`.

- No administra directamente las colecciones
- No contiene lógica de validación compleja
- Delega todo a `Restaurante` y a los modelos

**Principio SOLID aplicado:** Single Responsibility (S) — Solo coordina la interacción usuario-sistema.

## Relación entre Producto y Bebida

### Relación de Herencia

`Bebida` es una **subclase de `Producto`**, lo que significa que:

1. **Bebida hereda atributos de Producto:**
   - `codigo`, `nombre`, `categoria`, `precio`

2. **Bebida añade atributos específicos:**
   - `tamano`, `envase`

3. **Bebida sobrescribe el método `mostrar_informacion()`:**
   - Llamando a `super().mostrar_informacion()` para obtener la información base
   - Añadiendo información específica de bebida

### Ejemplo de Polimorfismo

```python
# Ambos pueden almacenarse en la misma lista
productos = Restaurante()
productos.registrar_producto(Producto("P1", "Pan", "Alimentos", 5.0))
productos.registrar_producto(Bebida("B1", "Agua", "Bebidas", 2.0, "500ml", "botella"))

# Ambos responden al mismo método (polimorfismo)
for producto in productos.listar_productos():
    print(producto)  # Cada uno muestra su información apropiada
```

**Principio SOLID aplicado:** Liskov Substitution Principle (L) — `Bebida` puede usarse donde se espera `Producto` sin errores.

## Principios SOLID Aplicados

### S — Single Responsibility Principle (SRP)
**"Cada clase debe tener una única razón para cambiar."**

En este proyecto:
- `Producto` solo representa datos de producto
- `Bebida` solo extiende con datos específicos de bebida
- `Cliente` solo representa datos de cliente
- `Restaurante` solo administra colecciones
- `main.py` solo maneja la interfaz

**Aplicación:** Cada clase tiene exactamente una responsabilidad bien definida.

### O — Open/Closed Principle (OCP)
**"Las clases deben estar abiertas para extensión pero cerradas para modificación."**

En este proyecto:
- `Restaurante` está **abierta para extensión**: Se puede crear `Platillo`, `Postre`, u otros tipos de productos
- `Restaurante` está **cerrada para modificación**: No necesita cambios para soportar nuevas subclases de `Producto`

**Ejemplo:**
```python
# Podría agregarse una nueva clase sin modificar Restaurante
class Platillo(Producto):
    def __init__(self, codigo, nombre, categoria, precio, tipo_coccion):
        super().__init__(codigo, nombre, categoria, precio)
        self.tipo_coccion = tipo_coccion
```

**Aplicación:** `Restaurante.listar_productos()` llama a `mostrar_informacion()` sin verificar el tipo específico.

### L — Liskov Substitution Principle (LSP)
**"Los objetos de una clase derivada deben poderse utilizar dondequiera que se use la clase base."**

En este proyecto:
- `Bebida` sustituye a `Producto` sin alterar el comportamiento esperado
- `Restaurante.registrar_producto()` acepta tanto `Producto` como `Bebida`
- El método `mostrar_informacion()` mantiene la misma firma en ambas clases

**Aplicación:** No hay validaciones de tipo ni casteos; el polimorfismo funciona naturalmente.

```python
def listar_productos(self) -> List[str]:
    # Funciona con Producto Y Bebida sin verificar tipos
    return [p.mostrar_informacion() for p in self._productos]
```

## Instrucciones de Ejecución

### 1. Requisitos
- Python 3.8 o superior
- No requiere librerías externas (solo la librería estándar)

### 2. Ejecutar el Programa

Desde la carpeta raíz del repositorio:

```bash
cd restaurante_app
python main.py
```

### 3. Menú Interactivo

El programa presentará un menú con las siguientes opciones:

```
========================================
        SISTEMA DE RESTAURANTE
========================================
1. Registrar producto
2. Registrar bebida
3. Registrar cliente
----------------------------------------
4. Listar productos
5. Listar clientes
----------------------------------------
6. Salir
```

### 4. Flujo de Uso

1. **Registrar Producto:**
   - Ingresa código, nombre, categoría y precio
   - Se valida que el código sea único y el precio > 0

2. **Registrar Bebida:**
   - Ingresa código, nombre, categoría, precio, tamaño y envase
   - Se valida que el código sea único y el precio > 0

3. **Registrar Cliente:**
   - Ingresa identificación, nombre y correo
   - Se valida que la ID sea única y el correo tenga formato válido

4. **Listar Productos:**
   - Muestra todos los productos y bebidas registrados
   - Cada uno con su información completa (usando polimorfismo)

5. **Listar Clientes:**
   - Muestra todos los clientes registrados

### 5. Validaciones Implementadas

- **Códigos de producto únicos:** No permite duplicados
- **IDs de cliente únicas:** No permite duplicados
- **Campos no vacíos:** Rechaza código, nombre o identificación vacíos
- **Precio positivo:** Requiere precio > 0 y formato numérico
- **Correo válido:** Valida formato básico de email

## Reflexión sobre Diseño Mantenible

### Importancia de los Principios SOLID

Un código bien diseñado siguiendo SOLID es más:

1. **Mantenible:** Cambios en una clase no afectan otras clases. Cada responsabilidad está aislada.

2. **Escalable:** Agregar nuevas funcionalidades (nuevos tipos de productos) es simple y seguro.

3. **Testeable:** Cada clase puede probarse de forma independiente sin acoplamiento fuerte.

4. **Flexible:** El polimorfismo permite que el código de alto nivel no dependa de detalles de bajo nivel.

### Aplicación en Este Proyecto

- **Mantenibilidad:** Si el formato de presentación de bebidas cambia, solo se modifica `Bebida.mostrar_informacion()`.

- **Escalabilidad:** Para agregar `Platillo`, basta crear una nueva clase que herede de `Producto` sin tocar `Restaurante`.

- **Testabilidad:** Cada clase puede instanciarse y probarse independientemente.

- **Flexibilidad:** `Restaurante` no necesita saber qué tipos específicos de productos maneja; funciona con cualquier subclase de `Producto`.

### Conclusión

Este proyecto demuestra que un diseño cuidadoso desde el inicio hace que el código sea más robusto, profesional y listo para evolucionar. Los principios SOLID no son restricciones, sino **guías para escribir software de calidad** que resista el paso del tiempo y los cambios inevitables que acompañan a cualquier proyecto real.

---

**Repositorio:** https://github.com/FernandoFernando876/2626-POO-Fernando-Fernandez

