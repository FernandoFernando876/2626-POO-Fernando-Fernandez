# restaurante_app (Parcial 1 - Semana 8)

Proyecto que implementa un sistema completo para registrar productos, bebidas y clientes
usando Programación Orientada a Objetos en Python. El proyecto demuestra principios SOLID,
validaciones de entrada, polimorfismo y pruebas unitarias con pytest.

## Estructura del Proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py        # Clase Producto (clase base)
│   ├── bebida.py          # Clase Bebida (hereda de Producto)
│   └── cliente.py         # Clase Cliente
├── servicios/
│   ├── __init__.py
│   └── restaurante.py     # Servicio que administra productos y clientes
├── tests/
│   ├── __init__.py
│   ├── conftest.py        # Configuración de pytest
│   └── test_restaurante.py # Pruebas unitarias
├── main.py                # Menú interactivo principal
├── pytest.ini             # Configuración de pytest
├── requirements.txt       # Dependencias del proyecto
└── README.md              # Este archivo
```

## Requisitos

- Python 3.8 o superior
- pytest (para ejecutar las pruebas)

## Instalación

1. Clonar el repositorio y navegar a la carpeta:
```bash
cd "Parcial 1\Semana 8\restaurante_app"
```

2. (Opcional) Crear un entorno virtual:
```bash
python -m venv venv
source venv/Scripts/activate  # En Windows PowerShell o cmd.exe
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Ejecución del Programa Principal

Desde la carpeta `restaurante_app`, ejecuta:
```bash
python main.py
```

El menú interactivo ofrece las siguientes opciones:
1. Registrar producto
2. Registrar bebida
3. Registrar cliente
4. Listar productos
5. Listar clientes
6. Salir
7. Explicación didáctica (SOLID)

## Ejecución de Pruebas

Ejecuta las pruebas unitarias desde la carpeta `restaurante_app`:
```bash
python -m pytest -v
```

O simplemente:
```bash
pytest
```

Resultado esperado: 3 pruebas pasadas (test_registrar_producto_bebida_y_listar, test_registrar_cliente_y_validar_duplicado, test_mostrar_informacion_polimorfismo).

## Principios SOLID Aplicados

**S - Single Responsibility**: Cada clase tiene una única responsabilidad clara.
  - `Producto` y `Bebida` representan datos y su presentación.
  - `Cliente` representa un cliente.
  - `Restaurante` administra registro y listado.
  - `main.py` maneja únicamente la interacción con el usuario.

**O - Open/Closed**: `Restaurante` opera sobre la interfaz de `Producto`, permitiendo extender
  el sistema con nuevas subclases (p.ej. `Platillo`) sin modificar el servicio.

**L - Liskov Substitution**: `Bebida` se puede usar donde se espera `Producto`. El servicio
  llama a `mostrar_informacion()` sin preguntar el tipo concreto del objeto (polimorfismo).

## Validaciones Implementadas

- Códigos de producto únicos (no se permiten duplicados).
- Identificaciones de cliente únicas (no se permiten duplicados).
- Código y nombre no pueden quedar vacíos.
- Precio debe ser numérico y mayor que 0.
- Correo debe tener formato válido (básico: contiene @).

## Características Principales

- Menú interactivo en consola con 7 opciones.
- Registro de productos y bebidas en una misma colección (polimorfismo).
- Listado de productos y clientes con formateo.
- Explicación didáctica interactiva sobre SOLID y responsabilidades.
- Anotaciones de tipos en constructores y métodos.
- Pruebas unitarias que verifican:
  - Registro y listado de productos y bebidas.
  - Validación de duplicados.
  - Polimorfismo de `mostrar_informacion()`.

## Notas

- Los archivos de módulos están organizados en paquetes (`modelos/`, `servicios/`) para
  facilitar la mantenibilidad y escalabilidad.
- Los archivos `__init__.py` están presentes en todos los paquetes.
- La explicación didáctica (opción 7) muestra ejemplos en tiempo real de cómo se aplican
  los principios SOLID en el sistema.

## Solución de Problemas

### Error: ModuleNotFoundError al ejecutar tests desde PyCharm

Asegúrate de ejecutar pytest desde la carpeta `restaurante_app`:
```bash
cd "Parcial 1\Semana 8\restaurante_app"
python -m pytest
```

El archivo `conftest.py` en la carpeta `tests/` ajusta automáticamente `sys.path` para resolver las importaciones.

### Advertencias de Linting en PyCharm

PyCharm puede mostrar advertencias de "Unresolved attribute reference" para atributos de clases.
Estas son falsos positivos y no afectan la ejecución del código. El código funciona correctamente
y todas las pruebas pasan.
   └── restaurante.py

