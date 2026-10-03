# Restaurante App - Semana 16

Aplicación de escritorio en Tkinter que continúa el sistema del restaurante
desarrollado en las semanas anteriores. Conserva el inicio de sesión, la
navegación, los productos y las ventas, y amplía la administración de usuarios
con una tabla, un formulario y eventos de interfaz.

## Gestión de usuarios

El modelo `Usuario` conserva los datos de acceso y agrega el rol
**Administrador**, **Empleado** o **Cliente**. El usuario Administrador puede
registrar, consultar, actualizar y eliminar usuarios Empleado y Cliente.
Empleados y Clientes mantienen el acceso a las secciones operativas, pero no
ven ni pueden abrir la administración de usuarios. La tabla muestra también
la cuenta Administrador para permitir consultarla, pero sus controles de
actualización y eliminación permanecen deshabilitados y el servicio rechaza
esas operaciones.

Cada usuario tiene un ID numérico estable, distinto de su nombre de usuario.
La tabla muestra ID, usuario, nombre y rol; no muestra contraseñas. Al
seleccionar una fila, `<<TreeviewSelect>>` activa un callback enlazado con
`bind()`. El callback toma el ID, consulta el objeto en
`RestauranteServicio` y carga los datos en el formulario. El botón **Consultar**
reutiliza esa consulta. La contraseña no se muestra y permanece sin cambios si
se deja en blanco al actualizar.

El Combobox de rol responde a `<<ComboboxSelected>>`. Los campos del
formulario aceptan `<Return>` para reutilizar el método de registro y
`<Escape>` para limpiar los datos y cancelar la selección. Los botones de
acción usan `command=`; sus operaciones y validaciones se delegan al servicio.
La eliminación solicita confirmación.

`RestauranteServicio` administra el CRUD y `ArchivoServicio` persiste los
usuarios, incluyendo su rol, en `datos/usuarios.json`. La misma capa de
servicios conserva la persistencia de productos y ventas. Los registros
anteriores a la incorporación de ID reciben uno al cargarse, y el rol faltante
se interpreta como Cliente, excepto el usuario `Admin`, que se reconoce como
Administrador.

## Estructura

```text
restaurante_app/
├── datos/                 # productos.json, usuarios.json y ventas.json
├── modelos/               # Producto, Usuario y Venta
├── servicios/             # ArchivoServicio y RestauranteServicio
├── ui/                    # LoginView y MainView
├── assets/                # logotipo e ícono de ventas
└── main.py
```

La interfaz no accede directamente a los archivos JSON: coordina las
interacciones y delega las reglas y la persistencia en los servicios.

## Ejecución

Ejecuta desde la carpeta `Parcial 2/Semana 16/restaurante_app` para abrir
esta versión de la aplicación:

```bash
python main.py
```

La ventana identifica esta entrega como **Restaurante App - Semana 16**.

Credenciales de demostración del administrador: `Admin / Admin123`.

## Eventos principales

| Interacción | Mecanismo | Respuesta |
|---|---|---|
| Selección en la tabla | `bind("<<TreeviewSelect>>", ...)` | Busca por ID y carga el usuario seleccionado |
| Botón Consultar | `command=` | Consulta el usuario de la fila seleccionada |
| Confirmación desde el formulario | `bind("<Return>", ...)` | Reutiliza el método de registro |
| Cancelación desde el formulario | `bind("<Escape>", ...)` | Limpia el formulario y la selección |
| Selección de rol | `bind("<<ComboboxSelected>>", ...)` | Actualiza el mensaje de estado |
| Botones Registrar, Actualizar, Eliminar y Limpiar | `command=` | Ejecutan los callbacks de cada operación |
