# ⚡ INICIO RÁPIDO - Sistema de Restaurante

## 🎬 En 2 Minutos

### Paso 1: Abrir Terminal

```powershell
cd "C:\Users\FERNANDO\Desktop\Nuevo repositorio\Parcial 1\Semana 7\restaurante_app"
```

### Paso 2: Ejecutar

```powershell
python main.py
```

### Paso 3: ¡Usar el Menú!

```
Seleccione una opción: 2  ← Presiona 2 y Enter para listar productos
```

---

## 🎮 Menú Quick Reference

| Tecla | Acción | Ejemplo |
|-------|--------|---------|
| `1` | Registrar producto | Ingresa: Pizza Pepperoni / Platillo / 13.50 |
| `2` | Listar productos | Ver todos los 7 productos |
| `3` | Buscar producto | Busca "Pizza" o categoría "Bebida" |
| `4` | Registrar cliente | Ingresa: C005 / Juan / juan@email.com |
| `5` | Listar clientes | Ver todos los 4 clientes |
| `6` | Buscar cliente | Busca por nombre o ID |
| `0` | Ver resumen | Total de productos y clientes |
| `7` | Salir | Termina el programa |

---

## 📚 Archivos Generados

```
restaurante_app/
├── modelos/
│   ├── __init__.py           ← Módulo vacío (requerido)
│   ├── producto.py           ← Clase Producto (constructor + setters)
│   └── cliente.py            ← Clase Cliente (@dataclass)
│
├── servicios/
│   ├── __init__.py           ← Módulo vacío (requerido)
│   └── restaurante.py        ← Clase Restaurante (gestión)
│
├── main.py                   ← Menú interactivo principal
├── README.md                 ← Documentación completa
├── GUIA_DE_USO.md           ← Guía detallada
├── RESUMEN_EJECUTIVO.md     ← Resumen del proyecto
└── INICIO_RAPIDO.md         ← Este archivo
```

---

## ✅ Lo que Demuestra

```
✅ Constructores tradicionales (__init__)
   └─ Visto en: Producto

✅ @property y @setter
   └─ Visto en: Producto.nombre, Producto.categoria, Producto.precio

✅ Validaciones de datos
   └─ Precio > 0, Nombre no vacío, Categoría no vacía

✅ Decorador @dataclass
   └─ Visto en: Cliente

✅ Arquitectura por capas
   └─ Modelos → Servicios → Presentación

✅ Creación de objetos desde input()
   └─ El usuario ingresa datos → Se crean objetos → Se almacenan

✅ Búsqueda y listado
   └─ Todos los productos/clientes se pueden listar y buscar
```

---

## 🎯 Casos de Uso Comunes

### Caso 1: Registrar un Producto Nuevo

```
Opción: 1

Nombre: Milanesa
Categoría: Platillo
Precio: 10.99

✅ Resultado: Producto creado y almacenado
```

### Caso 2: Buscar un Producto

```
Opción: 3
Submenu: 1 (Buscar por nombre)
Buscar: Pizza

✅ Resultado: Se muestran todos los productos con "Pizza"
```

### Caso 3: Ver Estadísticas

```
Opción: 0

✅ Resultado:
   📦 Productos registrados: 7 (o más si agregaste)
   👥 Clientes registrados: 4
```

---

## 🔍 Ejemplos de Búsqueda

### Buscar Productos por Nombre

```
Ingrese el nombre: Hamburguesa

RESULTADO:
1. ✅ Hamburguesa Clásica (Platillo) - $8.50
```

### Buscar Productos por Categoría

```
Ingrese la categoría: Bebida

RESULTADO:
1. ✅ Coca-Cola (Bebida) - $2.50
2. ✅ Jugo Natural (Bebida) - $3.50
```

### Buscar Cliente por Nombre

```
Ingrese el nombre: María

RESULTADO:
1. 👤 María López (ID: C002) - maria.lopez@email.com
```

### Buscar Cliente por ID

```
Ingrese el ID: C001

RESULTADO:
👤 Juan García (ID: C001) - juan.garcia@email.com
```

---

## 🚨 Errores Comunes

### Error: "No module named 'servicios'"

**Causa**: No estás en la carpeta correcta
**Solución**: 
```powershell
cd "C:\Users\FERNANDO\Desktop\Nuevo repositorio\Parcial 1\Semana 7\restaurante_app"
```

### Error: "El precio debe ser mayor que cero"

**Causa**: Ingresaste un precio negativo o cero
**Solución**: Ingresa un número positivo

### Error: "El nombre no puede estar vacío"

**Causa**: Dejaste el campo en blanco
**Solución**: Ingresa un nombre válido

---

## 💡 Tips & Tricks

### Tip 1: Búsqueda Parcial
Puedes buscar "Pizza" y encontrará "Pizza Margherita"

### Tip 2: Búsqueda Insensible a Mayúsculas
Puedes buscar "BEBIDA" y encontrará "Bebida"

### Tip 3: Datos de Ejemplo
Al iniciar, ya hay 7 productos y 4 clientes cargados

### Tip 4: Sin Datos Persistentes
Cuando cierres el programa, los datos que agregues se pierden (mejora futura)

### Tip 5: Validaciones Automáticas
No es posible ingresar datos inválidos - el programa rechaza automáticamente

---

## 📊 Datos Precargados

### Productos
1. Hamburguesa Clásica - $8.50
2. Pizza Margherita - $12.00
3. Ensalada César - $9.99
4. Coca-Cola - $2.50
5. Jugo Natural - $3.50
6. Flan Casero - $4.00
7. Brownie Chocolatero - $5.50

### Clientes
1. C001 - Juan García - juan.garcia@email.com
2. C002 - María López - maria.lopez@email.com
3. C003 - Carlos Rodríguez - carlos.rodriguez@email.com
4. C004 - Ana Martínez - ana.martinez@email.com

---

## 🔬 Concepto Demostrado: Constructor

```python
# Cuando presionas opción "1" e ingresas datos:
nombre = "Milanesa"        # ← input() del usuario
categoria = "Platillo"     # ← input() del usuario
precio = "10.99"           # ← input() del usuario

# Internamente ocurre esto:
nuevo_producto = Producto(
    nombre=nombre,         # ← Se pasa al constructor
    categoria=categoria,   # ← Se pasa al constructor
    precio=precio          # ← Se pasa al constructor
)
# El constructor __init__ VALIDA estos datos
# Si son válidos: objeto creado
# Si son inválidos: ValueError
```

---

## 🔬 Concepto Demostrado: @property y @setter

```python
# Cuando internamente se asigna un precio:
self.nombre = "Milanesa"

# Python hace esto:
@nombre.setter
def nombre(self, valor):
    if not valor or not str(valor).strip():
        raise ValueError("El nombre no puede estar vacío")
    self._nombre = str(valor).strip()

# Si el valor es válido → se asigna
# Si el valor es inválido → error
```

---

## 🔬 Concepto Demostrado: @dataclass

```python
# En lugar de escribir esto para Cliente:
class Cliente:
    def __init__(self, id_cliente, nombre, correo):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.correo = correo
    
    def __repr__(self):
        return f"Cliente({self.id_cliente}, {self.nombre}, {self.correo})"

# Escribimos esto:
@dataclass
class Cliente:
    id_cliente: str
    nombre: str
    correo: str
# ¡@dataclass genera todo automáticamente!
```

---

## 🔬 Concepto Demostrado: Arquitectura por Capas

```
OPCIÓN 5 (Listar clientes)
    ↓
main.py: listar_clientes()
    ↓
restaurante.listar_clientes()        [CAPA DE SERVICIOS]
    ↓
for cliente in self._clientes:       [ACCEDE A LISTA]
    ↓
print(cliente)                        [CAPA DE PRESENTACIÓN]
    ↓
Cliente.__str__()                    [CAPA DE MODELOS]
```

Cada capa tiene su responsabilidad:
- Modelos: Define QUÉ es un cliente
- Servicios: Administra CÓMO se almacenan
- Presentación: Decide CÓMO se muestran

---

## 📖 Para Aprender Más

1. **Lee el código en**:
   - `modelos/producto.py` ← Entiende @property y @setter
   - `modelos/cliente.py` ← Entiende @dataclass
   - `servicios/restaurante.py` ← Entiende gestión de listas
   - `main.py` ← Entiende el menú

2. **Experimenta**:
   - Intenta registrar productos inválidos
   - Busca con diferentes términos
   - Registra nuevos clientes
   - Observa cómo funciona todo

3. **Modifica (para aprender)**:
   - Agregua un nuevo atributo a Producto
   - Crea nuevas búsquedas
   - Cambia los mensajes de validación

---

## ✨ Características Destacadas

✅ **Menú intuitivo**: Fácil de usar
✅ **Datos ejemplo**: No necesitas ingresar nada para empezar
✅ **Validaciones robustas**: No acepta datos inválidos
✅ **Búsquedas potentes**: Por nombre, categoría, ID
✅ **Código limpio**: Fácil de entender y modificar
✅ **Bien documentado**: 300+ líneas de comentarios
✅ **Didáctico**: Enseña conceptos POO reales

---

## 🎓 Conclusión

Este proyecto demuestra que entiendes:

```
✅ Cómo crear objetos seguros con constructores
✅ Cómo proteger datos con @property y @setter
✅ Cómo simplificar código con @dataclass
✅ Cómo organizar código en capas
✅ Cómo crear interfaces amigables para el usuario
✅ Cómo almacenar y buscar datos
```

**¡Felicidades! 🎉**

---

**Presiona `7` para salir cuando termines.**

