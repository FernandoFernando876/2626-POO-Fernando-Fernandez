# 2626-POO-Fernando-Fernandez

## 👤 Información del Estudiante
**Nombre:** Robert Fernando Fernández Llori

---

## 📚 Descripción del Repositorio

Este repositorio contiene todas las actividades y proyectos desarrollados en el curso de **Programación Orientada a Objetos (POO)** en Python durante el Parcial 1.

El objetivo principal es aprender y demostrar:
- Conceptos fundamentales de POO (encapsulación, abstracción, herencia, polimorfismo)
- Organización modular de proyectos
- Separación de responsabilidades
- Uso correcto de importaciones entre módulos
- Buenas prácticas en desarrollo de software (PEP 8)

---

## 📁 Estructura del Repositorio

```
2626-POO-Fernando-Fernandez/
├── Parcial 1/
│   ├── Semana 3/
│   │   ├── Programacion Tradicional/
│   │   │   └── Tradicional.py
│   │   └── Programacion_POO/
│   │       ├── main.py
│   │       └── mascota.py
│   ├── Semana 4/
│   │   └── Proyecto 1/
│   │       ├── README.md
│   │       └── Restaurante_App/
│   │           ├── main.py
│   │           ├── Modelos_/
│   │           │   ├── Productos.py
│   │           │   └── Clientes.py
│   │           └── Servicios_/
│   │               └── Restaurante.py
│   ├── Semana 5/
│   │   └── restaurante_app/
│   │       ├── README.md
│   │       ├── main.py
│   │       ├── modelos/
│   │       │   ├── __init__.py
│   │       │   ├── producto.py
│   │       │   └── cliente.py
│   │       └── servicios/
│   │           ├── __init__.py
│   │           └── restaurante.py
│   ├── Semana 6/
│   │   └── restaurante_app/
│   │       ├── README.md
│   │       ├── main.py
│   │       ├── modelos/
│   │       │   ├── __init__.py
│   │       │   ├── producto.py    ← Clase base (padre)
│   │       │   ├── platillo.py    ← Clase hija (Herencia)
│   │       │   └── bebida.py      ← Clase hija (Herencia)
│   │       └── servicios/
│   │           ├── __init__.py
│   │           └── restaurante.py
│   └── Semana 7/
│       └── (en desarrollo)
├── main.py
├── .gitignore
└── README.md
```

---

## 🎯 Proyectos Destacados

### Parcial 1 - Semana 4: Proyecto 1

**Sistema de Gestión de Restaurante con POO**

Un sistema modular que demuestra la aplicación de Programación Orientada a Objetos en un contexto real: la gestión de un restaurante.

#### Características:
- ✅ Estructura modular (modelos, servicios)
- ✅ Clases: Producto, Cliente, Restaurante
- ✅ Métodos especiales (`__init__`, `__str__`)
- ✅ Gestión de productos y clientes
- ✅ Importaciones correctas entre módulos
- ✅ Código comentado y documentado

👉 [README - Proyecto 1](./Parcial%201/Semana%204/Proyecto%201/README.md)

---

### Parcial 1 - Semana 5: Sistema de Restaurante v2

**Sistema ampliado con tipos de datos y anotaciones**

Versión mejorada del sistema de restaurante aplicando convenciones de nombres, tipos de datos y anotaciones de tipo.

#### Características:
- ✅ Anotaciones de tipo (`str`, `int`, `float`, `bool`, `List`)
- ✅ PascalCase para clases, snake_case para métodos y variables
- ✅ Clases: Producto, Cliente, Restaurante
- ✅ Métodos de gestión para agregar, modificar y consultar
- ✅ Estructura modular escalable

👉 [README - Semana 5](./Parcial%201/Semana%205/restaurante_app/README.md)

---

### Parcial 1 - Semana 6: Sistema de Restaurante v3 (Herencia & Polimorfismo)

**Sistema con Herencia, Encapsulación y Polimorfismo**

Versión avanzada que implementa los tres pilares de POO de forma explícita.

#### Características:
- ✅ **Herencia**: `Platillo` y `Bebida` heredan de `Producto`
- ✅ **Encapsulación**: Atributo `__precio` privado con getter/setter validado
- ✅ **Polimorfismo**: Método `mostrar_informacion()` sobreescrito en cada subclase
- ✅ `super().__init__()` en constructores de clases hijas
- ✅ Validación con `ValueError` en setter de precio
- ✅ Estructura modular completa

👉 [README - Semana 6](./Parcial%201/Semana%206/restaurante_app/README.md)

---

## 🚀 Cómo Ejecutar los Proyectos

### Semana 4 - Proyecto 1:
```bash
cd "Parcial 1/Semana 4/Proyecto 1/Restaurante_App"
python main.py
```

### Semana 5:
```bash
cd "Parcial 1/Semana 5/restaurante_app"
python main.py
```

### Semana 6:
```bash
python "Parcial 1/Semana 6/restaurante_app/main.py"
```

### Requisitos
- Python 3.x instalado
- Sin dependencias externas requeridas

---

## 📖 Temas Cubiertos

### Parcial 1

- **Semana 3:**
  - Programación Tradicional vs POO
  - Introducción a clases y objetos
  - Ejemplo práctico con Mascota

- **Semana 4:**
  - Proyecto 1: Sistema de Gestión de Restaurante
  - Modularización de proyectos
  - Separación de responsabilidades
  - Importaciones entre módulos

- **Semana 5:**
  - Tipos de datos y anotaciones de tipo
  - Convenciones de nombres (PEP 8)
  - Listas como tipo compuesto
  - Métodos getters/setters básicos

- **Semana 6:**
  - **Herencia** (clase padre → clases hijas)
  - **Encapsulación** (atributos privados `__nombre`)
  - **Polimorfismo** (sobreescritura de métodos)
  - `super()` para inicializar herencia
  - Validación con excepciones (`ValueError`)

- **Semana 7:**
  - *(En desarrollo)*

---

## 💡 Conceptos POO Aplicados

| Concepto | Descripción | Semana |
|---|---|---|
| **Clases y Objetos** | Definición y uso de clases | Sem 3-4 |
| **Encapsulación** | Atributos privados con `__` y métodos getter/setter | Sem 6 |
| **Abstracción** | Ocultación de detalles en métodos | Sem 4-5 |
| **Herencia** | Reutilización de código con `super()` | Sem 6 |
| **Polimorfismo** | Sobreescritura de `mostrar_informacion()` | Sem 6 |
| **Modularización** | Organización en paquetes y módulos | Sem 4-6 |
| **Métodos Especiales** | `__init__()`, `__str__()` | Sem 3-5 |

---

## 📝 Notas de Desarrollo

- Todos los proyectos son desarrollados en **Python 3.x**
- Se sigue la **PEP 8** para estilo de código
- Los comentarios están en español para mejor comprensión
- Se enfatiza la claridad y modularización sobre la complejidad

---

## 🔄 Historial de Cambios

Para ver el historial completo de commits, ejecuta:

```bash
git log --oneline
```

---

## 📧 Contacto

**Estudiante:** Robert Fernando Fernández Llori

---

**Última actualización:** Agosto 2026

**Estado:** En desarrollo 🚀

