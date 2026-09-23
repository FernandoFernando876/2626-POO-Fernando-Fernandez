# Restaurante App - Semana 15

Aplicación de escritorio en Tkinter para administrar usuarios, productos y ventas
de un restaurante. Esta entrega evoluciona la aplicación de las semanas
anteriores sin reconstruir su arquitectura modular.

## Flujo de ventas

En la pestaña **Ventas**, el usuario selecciona un usuario y un producto en
componentes `ttk.Combobox`, indica la cantidad y presiona **Registrar Venta**.
El botón usa `command=self._registrar_venta`; el callback obtiene los valores,
delega la validación y el registro a `RestauranteServicio`, y actualiza la
tabla y el mensaje visual. El servicio descuenta el stock y utiliza
`ArchivoServicio` para persistir la venta en `datos/ventas.json`.

Cada venta conserva usuario, producto, cantidad y fecha. Al reiniciar la
aplicación, las ventas se recuperan desde el JSON. También se conserva el
precio unitario y el total calculado automáticamente.

La ventana de login muestra las credenciales del administrador para facilitar
el acceso durante la demostración. En la pestaña Ventas se presentan los
detalles del cliente y del producto seleccionado, junto con el total
actualizado a partir de `cantidad * precio unitario`.

## Estructura

```text
restaurante_app/
├── datos/                 # productos.json, usuarios.json y ventas.json
├── modelos/               # Producto, Usuario y Venta
├── servicios/             # ArchivoServicio y RestauranteServicio
├── ui/                    # LoginView y MainView
├── assets/                # logo.svg y ventas.svg
└── main.py
```

La interfaz no lee ni escribe archivos JSON directamente: esa responsabilidad
pertenece a los servicios.

## Ejecución

Desde la raíz del repositorio:

```bash
python restaurante_app/main.py
```

También puede ejecutarse desde la carpeta del proyecto:

```bash
cd restaurante_app
python main.py
```

Credenciales incluidas: `mesero / mesero123`.
