# Semana 13 - Restaurante App

Esta carpeta contiene la base gráfica del proyecto `restaurante_app` correspondiente a la Semana 13.

## Objetivo
Implementar una estructura modular con:
- modelos para Producto y Usuario,
- servicio para lectura de JSON y validación de acceso,
- vistas de login y panel principal,
- una sola ventana de Tkinter para cambiar entre pantallas.

## Estructura

```text
Semana 13/
├── restaurante_app/
│   ├── datos/
│   │   ├── productos.json
│   │   └── usuarios.json
│   ├── modelos/
│   │   ├── __init__.py
│   │   ├── producto.py
│   │   └── usuario.py
│   ├── servicios/
│   │   ├── __init__.py
│   │   ├── archivo_servicio.py
│   │   └── restaurante_servicio.py
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── login_view.py
│   │   └── main_view.py
│   ├── main.py
│   └── README.md
└── README.md
```

## Ejecución

```bash
cd "Parcial 2/Semana 13/restaurante_app"
python main.py
```
