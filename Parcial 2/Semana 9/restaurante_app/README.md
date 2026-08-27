# Sistema de Gestión de Restaurante (Semana 9 - Parcial 2)

**Estudiante:** Robert Fernando Fernández Llori

Descripción y estructura similar a la entrega previa. Este directorio contiene la versión del proyecto organizada para la carpeta Parcial 2 - Semana 9.

Estructura mínima:

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── bebida.py
│   ├── cliente.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py
```

Uso de estructuras:
- list: almacenamiento dinámico de `_productos` y `_usuarios`.
- tuple: `MENU_OPTIONS` en `main.py` fija las opciones del menú.
- dict: `menu_actions` para asociar opción → función.
- set: `Restaurante.obtener_categorias_unicas()` devuelve categorías únicas.

Instrucciones de ejecución:

```powershell
cd "C:\Users\FERNANDO\Desktop\Nuevo repositorio\Parcial 2\Semana 9\restaurante_app"
python main.py
```

