# 2626-POO-Fernando-Fernandez

## 👤 Información del Estudiante
**Nombre:** Robert Fernando Fernández Llori
**Curso:** Programación Orientada a Objetos (POO)
**Repositorio:** https://github.com/FernandoFernando876/2626-POO-Fernando-Fernandez

---

## 📚 Descripción del Repositorio

Este repositorio contiene todas las actividades y proyectos desarrollados en el curso de **Programación Orientada a Objetos (POO)** en Python durante los Parciales 1 y 2.

El objetivo principal es aprender y demostrar:
- Conceptos fundamentales de POO (encapsulación, abstracción, herencia, polimorfismo)
- Principios de diseño SOLID
- Organización modular de proyectos
- Separación de responsabilidades
- Uso correcto de importaciones entre módulos
- Persistencia de datos con JSON
- Pruebas automatizadas con pytest
- Buenas prácticas en desarrollo de software (PEP 8)

---

## 📁 Estructura del Repositorio

```
2626-POO-Fernando-Fernandez/
├── Parcial 1/
│   ├── Semana 3/       # Intro POO vs Tradicional
│   ├── Semana 4/       # Proyecto 1: Sistema modular básico
│   ├── Semana 5/       # Tipos de datos y anotaciones
│   ├── Semana 6/       # Herencia, Encapsulación, Polimorfismo
│   ├── Semana 7/       # @property, @dataclass, menú interactivo
│   └── Semana 8/       # Validaciones + Tests pytest
├── Parcial 2/
│   ├── Semana 9/       # Principios SOLID + Estructuras de datos
│   └── Semana 10/      # Persistencia JSON
├── restaurante_app/    # Versión más reciente
├── main.py
├── .gitignore
└── README.md
```

---

## 🎯 Proyectos por Semana

### 📌 Parcial 1

#### Semana 3 — Introducción a POO
Comparación entre programación tradicional y POO. Primer ejemplo con clase Mascota.

#### Semana 4 — Sistema de Restaurante v1
Primera versión modular con clases Producto, Cliente y Restaurante.
👉 [README - Semana 4](./Parcial%201/Semana%204/Proyecto%201/README.md)

#### Semana 5 — Tipos de Datos y Anotaciones
Versión mejorada con anotaciones de tipo y convenciones PEP 8.
- Anotaciones: str, int, float, bool, List
👉 [README - Semana 5](./Parcial%201/Semana%205/restaurante_app/README.md)

#### Semana 6 — Herencia, Encapsulación y Polimorfismo
Los tres pilares de POO aplicados explícitamente.
- Herencia: Platillo y Bebida heredan de Producto
- Encapsulación: atributo __precio con getter/setter validado
- Polimorfismo: mostrar_informacion() sobreescrito
👉 [README - Semana 6](./Parcial%201/Semana%206/restaurante_app/README.md)

#### Semana 7 — Decoradores @property y @dataclass
Decoradores modernos de Python y menú interactivo con 8 opciones.
- @property y @setter en clase Producto
- @dataclass en clase Cliente
👉 [README - Semana 7](./Parcial%201/Semana%207/restaurante_app/README.md)

#### Semana 8 — Validaciones y Tests con pytest
Sistema con validaciones robustas y pruebas automatizadas.
- Validaciones de precio, email y campos vacíos
- Tests con pytest
👉 [README - Semana 8](./Parcial%201/Semana%208/restaurante_app/README.md)

---

### 📌 Parcial 2

#### Semana 9 — Principios SOLID y Estructuras de Datos
Sistema completo con principios SOLID y las 4 estructuras de datos de Python.
- S: Single Responsibility — cada clase con una responsabilidad
- O: Open/Closed — abierta para extensión, cerrada para modificación
- L: Liskov Substitution — Bebida sustituye a Producto
- list, tuple, dict, set aplicados funcionalmente
👉 [README - Semana 9](./Parcial%202/Semana%209/restaurante_app/README.md)

#### Semana 10 — Persistencia de Datos con JSON
Sistema con lectura y escritura de archivos JSON.
- Servicio ArchivoServicio para persistencia
- Archivo datos/productos.json
👉 [README - Semana 10](./Parcial%202/Semana%2010/restaurante_app/README.md)

---

## 🚀 Cómo Ejecutar los Proyectos

### Versión más reciente (raíz):
```bash
cd restaurante_app
python main.py
```

### Semana 9 (SOLID):
```bash
python "Parcial 2/Semana 9/restaurante_app/main.py"
```

### Semana 8 (con tests):
```bash
cd "Parcial 1/Semana 8/restaurante_app"
python main.py
pytest tests/
```

### Requisitos
- Python 3.8+ instalado
- Para tests: pip install pytest

---

## 📖 Temas Cubiertos por Semana

| Semana | Parcial | Tema Principal | Conceptos Clave |
|--------|---------|----------------|-----------------|
| Sem 3  | P1 | Intro a POO | Clases, objetos, __init__, __str__ |
| Sem 4  | P1 | Sistema modular | Modelos, servicios, importaciones |
| Sem 5  | P1 | Tipos y anotaciones | List, type hints, PEP 8 |
| Sem 6  | P1 | Pilares de POO | Herencia, encapsulación, polimorfismo |
| Sem 7  | P1 | Decoradores | @property, @dataclass, menú |
| Sem 8  | P1 | Calidad de código | Validaciones, pytest, tests |
| Sem 9  | P2 | SOLID | SRP, OCP, LSP, estructuras de datos |
| Sem 10 | P2 | Persistencia | JSON, lectura/escritura de archivos |

---

## 💡 Conceptos POO Aplicados

| Concepto | Descripción | Semana |
|---|---|---|
| Clases y Objetos | Definición y uso de clases | Sem 3-4 |
| Encapsulación | Atributos privados __ con getter/setter | Sem 6+ |
| Abstracción | Ocultación de detalles en métodos | Sem 4-5 |
| Herencia | Reutilización de código con super() | Sem 6+ |
| Polimorfismo | Sobreescritura de métodos | Sem 6+ |
| Modularización | Organización en paquetes y módulos | Sem 4-10 |
| @property | Decoradores para getters/setters | Sem 7 |
| @dataclass | Clases de datos simplificadas | Sem 7 |
| Principios SOLID | Diseño orientado a calidad | Sem 9 |
| Persistencia JSON | Lectura/escritura de archivos | Sem 10 |

---

## 📝 Notas de Desarrollo

- Todos los proyectos son desarrollados en **Python 3.8+**
- Se sigue la **PEP 8** para estilo de código
- Los comentarios están en español para mejor comprensión
- Se enfatiza la claridad y modularización sobre la complejidad

---

## 🔄 Historial de Cambios

```bash
git log --oneline
```

---

**Última actualización:** Agosto 2026

**Estado:** En desarrollo 🚀
