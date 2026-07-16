# restaurante_app (Parcial 1 - Semana 8)

Proyecto de ejemplo que implementa un sistema simple para registrar productos, bebidas y clientes
usando Programación Orientada a Objetos en Python. La estructura del proyecto respeta la separación
de responsabilidades y demuestra principios SOLID de forma didáctica.

Estructura:
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── bebida.py
│   └── cliente.py
├── servicios/
│   ├── __init__.py
   └── restaurante.py
└── main.py

Principios SOLID aplicados (resumen):
- S (Single Responsibility): Cada clase tiene una única responsabilidad (Producto/Bebida, Cliente, Restaurante).
- O (Open/Closed): Se puede extender con nuevas clases (por ejemplo, nuevas subclases de Producto) sin modificar `Restaurante`.
- L (Liskov Substitution): `Bebida` sustituye a `Producto` sin alterar el comportamiento del servicio; `Restaurante` trata a ambos por la interfaz común `mostrar_informacion()`.

Ejecución:
Abra una consola PowerShell, sitúese en:
`C:\Users\FERNANDO\Desktop\Nuevo repositorio\Parcial 1\Semana 8\restaurante_app`
y ejecute:
```
python main.py
```

Uso:
- El menú interactivo permite registrar productos, bebidas y clientes, así como listar los registros.
- Validaciones: no se permiten códigos de producto duplicados ni identificaciones de cliente repetidas.

Notas didácticas:
- `Producto.mostrar_informacion()` está diseñado para ser usado por el servicio sin preguntar qué tipo concreto es el objeto.
- La clase `Bebida` extiende `Producto` agregando atributos propios y sobrescribiendo `mostrar_informacion()`.

