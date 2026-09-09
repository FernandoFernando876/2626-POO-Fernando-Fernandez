# restaurante_app - Semana 13

Aplicación base con interfaz gráfica para un restaurante, siguiendo la organización modular de modelos, servicios, datos y vistas.

## Propósito
Esta versión mantiene una estructura clara para trabajar con:
- productos cargados desde JSON,
- usuarios para la simulación de acceso,
- una pantalla de login y una vista principal en la misma ventana,
- separación entre lógica del negocio y presentación gráfica.

## Estructura del proyecto

restaurante_app/
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── __init__.py
├── main.py
├── README.md
└── run_simulation.py

## Flujo de la aplicación
1. Se inicia la aplicación desde `main.py`.
2. Se crea una sola ventana de Tkinter.
3. Primero se muestra `LoginView`.
4. Se valida el usuario y la contraseña con `RestauranteServicio`.
5. Si el acceso es correcto, se muestra `MainView` dentro de la misma ventana.
6. Desde la vista principal se pueden consultar productos y usuarios cargados desde JSON.
7. La opción de cerrar sesión regresa al login sin crear otra ventana.

## Archivos principales
- `modelo/producto.py`: representa los productos del restaurante.
- `modelo/usuario.py`: representa los usuarios con acceso simulado.
- `servicios/archivo_servicio.py`: carga los datos desde archivos JSON.
- `servicios/restaurante_servicio.py`: centraliza la validación y consulta de usuarios/productos.
- `ui/login_view.py`: pantalla de inicio de sesión.
- `ui/main_view.py`: panel principal con opciones de consulta.
- `main.py`: prepara la ventana, conecta las vistas y controla el cambio entre login y panel principal.

## Cómo ejecutar
Desde la raíz del repositorio:

```bash
python main.py
```

O desde la carpeta del proyecto:

```bash
cd restaurante_app
python main.py
```

## Credenciales de prueba
Se utilizan usuarios simulados con contraseña en `datos/usuarios.json`:
- `admin` / `admin123`
- `mesero` / `mesero123`

## Nota
La aplicación base está diseñada para ser ampliada en semanas posteriores con más funcionalidades del restaurante, pero esta primera versión se mantiene enfocada en la organización modular y en el flujo correcto de login → panel principal.
