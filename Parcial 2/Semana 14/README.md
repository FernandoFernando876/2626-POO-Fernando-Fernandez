# Semana 14 - Restaurante App

Este proyecto corresponde a la evolución de la aplicación de restaurante para la Semana 14, manteniendo la estructura modular y mejorando la interfaz con contenedores, formularios, tablas y acciones de gestión.

## Estructura

- restaurante_app/
  - datos/
    - productos.json
    - usuarios.json
  - modelos/
    - __init__.py
    - producto.py
    - usuario.py
  - servicios/
    - __init__.py
    - archivo_servicio.py
    - restaurante_servicio.py
  - ui/
    - __init__.py
    - login_view.py
    - main_view.py
  - __init__.py
  - main.py

## Objetivo

La aplicación conserva el acceso con usuario y contraseña y agrega una interfaz principal organizada para consultar usuarios y gestionar productos del restaurante con operaciones básicas: registro, búsqueda, actualización y eliminación.

## Componentes y contenedores utilizados

Se emplean contenedores principales para separar:

- la zona de navegación,
- el formulario de productos,
- la presentación de los registros,
- la consulta de usuarios.

Además, se utilizan componentes como:

- Labels
- Entries
- Buttons
- Frames
- LabelFrame
- Treeview
- Scrollbar
- StringVar

## Operaciones implementadas

En la sección de Productos se puede:

- registrar un nuevo producto,
- consultar un producto por código,
- actualizar sus datos,
- eliminar un producto,
- visualizar la información actualizada en una tabla.

Las validaciones de negocio, como campos vacíos, precios positivos, stock válido y códigos duplicados, se mantienen dentro de RestauranteServicio.

## Persistencia

La información se guarda en los archivos JSON ubicados en `restaurante_app/datos/`, usando el servicio de archivos para leer y escribir la información.

## Ejecución

Desde la carpeta `Parcial 2/Semana 14`, ejecute:

```bash
python restaurante_app/main.py
```

O bien, dentro de la carpeta `restaurante_app`:

```bash
python main.py
```

## Credenciales de prueba

- Usuario: admin
- Contraseña: admin123
