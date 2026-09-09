# restaurante_app - Semana 13

Aplicación base para un restaurante con interfaz gráfica modular.

## Propósito
La aplicación permite:
- iniciar sesión en una pantalla de acceso simulada,
- revisar productos cargados desde JSON,
- revisar usuarios registrados,
- navegar dentro de la misma ventana usando Tkinter.

## Estructura

```text
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
├── main.py
└── README.md
```

## Flujo
1. `main.py` prepara la ventana principal.
2. Se muestra `LoginView` primero.
3. El servicio valida usuario y contraseña.
4. Si el acceso es correcto, se levanta `MainView`.
5. La vista principal muestra productos y usuarios.
6. La opción de cerrar sesión devuelve al login sin crear otra ventana.

## Ejecución

```bash
cd "Parcial 2/Semana 13/restaurante_app"
python main.py
```

## Credenciales de prueba
- usuario: `admin`
- contraseña: `admin123`
