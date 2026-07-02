# Semana 6 - Sistema de Gestión de Restaurante con Programación Orientada a Objetos

Este proyecto implementa una versión mejorada del sistema `restaurante_app` utilizando los conceptos fundamentales de la Programación Orientada a Objetos (POO) en Python: **Herencia, Encapsulación y Polimorfismo**, estructurado de forma completamente modular.

---

## 👤 Información del Estudiante
* **Nombre Completo:** Fernando Fernández
* **Curso/Asignatura:** Programación Orientada a Objetos (POO)
* **Período:** Parcial 1 - Semana 6

---

## 📝 Descripción del Sistema
El sistema modela la gestión del menú de un restaurante, administrando productos genéricos mediante una clase base y especializándolos en dos categorías principales: platillos de comida y bebidas. Permite registrar diversos artículos, controlar la disponibilidad, asegurar la integridad del precio mediante encapsulación y mostrar el menú completo en la consola haciendo uso de polimorfismo.

---

## 📂 Estructura del Proyecto
El proyecto está estructurado modularmente para separar responsabilidades de la siguiente manera:

```text
restaurante_app/
├── modelos/
│   ├── __init__.py      # Define las importaciones del paquete modelos
│   ├── producto.py      # Clase base padre (Producto)
│   ├── platillo.py      # Clase hija especializada (Platillo)
│   └── bebida.py        # Clase hija especializada (Bebida)
├── servicios/
│   ├── __init__.py      # Define las importaciones del paquete servicios
│   └── restaurante.py   # Servicio de gestión del menú (Restaurante)
├── main.py              # Punto de entrada y demostración funcional del sistema
└── README.md            # Documentación del proyecto (este archivo)
```

---

## 🧬 Principios de POO Aplicados

### 1. Herencia
Se implementó una jerarquía lógica de clases donde la clase base `Producto` comparte sus atributos y comportamiento a clases más especializadas:
* **Clase Padre (`Producto`):** Contiene atributos comunes a cualquier ítem del restaurante como `nombre` (str) y `disponible` (bool), además del atributo privado encapsulado para el precio.
* **Clase Hija (`Platillo`):** Hereda de `Producto` y añade el atributo específico `tiempo_preparacion` (en minutos).
* **Clase Hija (`Bebida`):** Hereda de `Producto` y añade el atributo específico `volumen_ml` (en mililitros).
* Se utilizó la función `super().__init__(...)` en el constructor de las clases hijas para inicializar correctamente los atributos heredados de la clase base.

### 2. Encapsulación
* **Atributo Encapsulado:** El precio del producto se declaró como privado en la clase padre utilizando el prefijo de doble guion bajo (`__precio`). Esto evita el acceso o la modificación directa accidental desde fuera del objeto.
* **Método Getter (`obtener_precio()`):** Permite consultar el precio de forma controlada.
* **Método Setter (`cambiar_precio()`):** Permite modificar el precio, implementando una **validación estricta** para asegurar que el nuevo valor sea estrictamente mayor que cero (`nuevo_precio > 0`). Si el precio ingresado es inválido (cero o negativo), se lanza una excepción de tipo `ValueError`.

### 3. Polimorfismo
* **Método Polimórfico:** `mostrar_informacion()`.
* **Implementación:** La clase base `Producto` define una implementación estándar del método. Tanto `Platillo` como `Bebida` **sobrescriben** (`override`) este método utilizando `super().mostrar_informacion()` para añadir sus propios detalles (tiempo de preparación para platillos y volumen en mililitros para bebidas).
* **Demostración:** Al recorrer la lista de productos dentro de `Restaurante.mostrar_menu()`, se invoca recursivamente `mostrar_informacion()`. Python ejecuta dinámicamente la versión del método correspondiente al tipo real de cada objeto (sea Platillo o Bebida) sin que el servicio necesite conocer los detalles específicos de cada tipo de producto de antemano.

---

## 💭 Reflexión sobre POO en Python Modular
La implementación de proyectos mediante Programación Orientada a Objetos y una estructura modular en Python ofrece grandes beneficios para el desarrollo de software moderno:
1. **Mantenibilidad y Escalabilidad:** Al organizar el código en archivos independientes con responsabilidades claras (modelos y servicios separados), es muy fácil añadir nuevas características. Por ejemplo, podríamos agregar un tipo de producto `Postre` o un servicio de `Ordenes` sin afectar el código existente.
2. **Reutilización de Código:** La herencia nos evita duplicar atributos comunes como nombre o precio en múltiples clases, reduciendo la redundancia de código y la probabilidad de errores.
3. **Seguridad y Control de Datos:** La encapsulación garantiza que los datos sensibles del negocio (como los precios) sigan reglas de validación predefinidas, impidiendo que el estado del sistema quede inconsistente o con datos inválidos.
4. **Legibilidad:** Dividir un sistema en módulos con nombres e interfaces claros permite que otros desarrolladores comprendan rápidamente la estructura del software, haciendo que el trabajo en equipo sea mucho más fluido y ordenado.

---

## 🚀 Instrucciones de Ejecución
Para ejecutar y probar el sistema, abra una terminal y ejecute el archivo principal `main.py` desde el directorio raíz de la aplicación:

```powershell
python "Parcial 1/Semana 6/restaurante_app/main.py"
```
