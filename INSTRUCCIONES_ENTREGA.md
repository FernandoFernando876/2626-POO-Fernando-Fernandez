# INSTRUCCIONES DE ENTREGA - SEMANA 10

## 🎯 Objetivo
Entregar el proyecto **Restaurante App - Semana 10** con persistencia de productos mediante JSON en un nuevo repositorio público de GitHub.

---

## 📋 Checklist Pre-Entrega

- ✅ Proyecto completado en `C:\Users\FERNANDO\Desktop\Nuevo repositorio\Parcial 2\Semana 10`
- ✅ Estructura modular verificada
- ✅ Todas las pruebas pasadas
- ✅ Documentación completa
- ✅ Archivos `__init__.py` presentes
- ✅ Archivo JSON creado y funcional
- ✅ Sin archivos innecesarios (solo .py, .md, .json, .txt)

---

## 🚀 PASOS PARA ENTREGAR EN GITHUB

### Paso 1: Crear un Nuevo Repositorio en GitHub
1. Ir a https://github.com/new
2. Nombre: `semana-10-persistencia-json`
3. Descripción: "Restaurante App - Semana 10: Persistencia de productos con JSON"
4. Visibilidad: **Público** ✅
5. NO inicializar con README (ya lo tenemos)
6. Click en "Create Repository"

### Paso 2: Preparar el Directorio Local

Abrir PowerShell y ejecutar:
```powershell
cd "C:\Users\FERNANDO\Desktop\Nuevo repositorio\Parcial 2\Semana 10"
```

### Paso 3: Inicializar Git
```powershell
git init
git add .
git commit -m "Semana 10: Persistencia de productos con JSON"
git branch -M main
```

### Paso 4: Conectar con GitHub
Reemplazar `<USUARIO>` por tu usuario de GitHub:
```powershell
git remote add origin https://github.com/<USUARIO>/semana-10-persistencia-json.git
git push -u origin main
```

**Ejemplo:**
```powershell
git remote add origin https://github.com/tu-usuario/semana-10-persistencia-json.git
git push -u origin main
```

### Paso 5: Verificar en GitHub
1. Ir a https://github.com/tu-usuario/semana-10-persistencia-json
2. Verificar que todos los archivos están presentes
3. Verificar que el README está visible
4. Confirmar que es público (sin candado)

---

## 📂 Estructura Esperada en GitHub

```
semana-10-persistencia-json/
├── README.md                                    ← Descripción general
├── CHECKLIST_ENTREGA.md                        ← Verificación
├── GUIA_PRUEBAS.md                             ← Guía de pruebas
├── RESUMEN_ENTREGA.md                          ← Resumen final
│
└── restaurante_app/
    ├── main.py                                  ← Punto de entrada
    ├── test_excepciones.py                     ← Pruebas
    ├── README.md                                ← Documentación técnica
    │
    ├── datos/
    │   └── productos.json                       ← Almacenamiento
    │
    ├── modelos/
    │   ├── __init__.py
    │   ├── producto.py
    │   ├── bebida.py
    │   └── usuario.py
    │
    └── servicios/
        ├── __init__.py
        ├── archivo_servicio.py
        └── restaurante.py
```

---

## 🔍 VERIFICACIONES FINALES

### Verificación Local Antes de Subir
```powershell
cd "C:\Users\FERNANDO\Desktop\Nuevo repositorio\Parcial 2\Semana 10\restaurante_app"

# Prueba 1: Ejecutar pruebas automatizadas
python test_excepciones.py

# Prueba 2: Verificar que no hay errores de sintaxis
python -m py_compile main.py modelos/producto.py servicios/archivo_servicio.py
```

### Verificación en GitHub
1. ✅ Archivo README.md se muestra correctamente
2. ✅ Todos los archivos .py están presentes
3. ✅ Archivo datos/productos.json existe
4. ✅ Archivos __init__.py están en paquetes
5. ✅ Documentación (CHECKLIST, GUIA, RESUMEN) está presente

---

## 📝 Información para la Entrega

Después de subir a GitHub, prepare la siguiente información:

**Datos para enviar:**
- **Enlace del repositorio:** https://github.com/[tu-usuario]/semana-10-persistencia-json
- **Nombre de estudiante:** [Tu nombre completo]
- **Semana:** 10
- **Estado:** Completado ✅

---

## 🎓 PUNTOS DE EVALUACIÓN

El docente revisará:

1. **Estructura del Proyecto** (10%)
   - ✅ Directorio modelos/, servicios/, datos/
   - ✅ Archivos __init__.py presentes
   - ✅ main.py como punto de entrada

2. **Persistencia JSON** (30%)
   - ✅ Productos se guardan en JSON
   - ✅ Productos se cargan al iniciar
   - ✅ Cambios se persisten entre ejecuciones
   - ✅ Archivo JSON tiene estructura correcta

3. **Operaciones CRUD** (20%)
   - ✅ Registrar productos
   - ✅ Buscar productos
   - ✅ Actualizar productos
   - ✅ Eliminar productos
   - ✅ Listar productos

4. **Manejo de Excepciones** (20%)
   - ✅ FileNotFoundError controlado
   - ✅ json.JSONDecodeError controlado
   - ✅ PermissionError contemplado
   - ✅ Registros inválidos omitidos
   - ✅ Programa no se detiene

5. **Documentación** (10%)
   - ✅ README.md documentado
   - ✅ Flujos explicados
   - ✅ Instrucciones claras
   - ✅ Ejemplos incluidos

6. **Código Limpio** (10%)
   - ✅ Anotaciones de tipos
   - ✅ Nombres descriptivos
   - ✅ Docstrings presentes
   - ✅ Sin código "quemado"

---

## 💡 CONSEJOS FINALES

1. **Antes de subir:**
   - Ejecutar `python test_excepciones.py`
   - Verificar que `main.py` funciona sin errores
   - Confirmar que JSON se crea y se actualiza

2. **En el repositorio:**
   - El README debe explicar claramente la mejora
   - La GUIA_PRUEBAS.md debe mostrar cómo probar
   - El CHECKLIST debe verificar cada requisito

3. **En la entrega:**
   - Enviar solo el enlace del repositorio
   - Asegurar que sea PÚBLICO y ACCESIBLE
   - Incluir nombre de estudiante en el README

4. **Si hay problemas:**
   - Verificar permisos (repositorio público)
   - Confirmar que git está instalado
   - Revisar que los archivos no sean demasiado grandes

---

## 📞 SOPORTE

Si necesitas ayuda, verifica:
- ✅ [README.md] - Descripción general
- ✅ [GUIA_PRUEBAS.md] - Cómo probar
- ✅ [CHECKLIST_ENTREGA.md] - Qué se verificó
- ✅ [RESUMEN_ENTREGA.md] - Resumen completo

---

## ✅ ESTADO FINAL

**El proyecto está LISTO PARA ENTREGAR**

- ✅ Código completo y funcional
- ✅ Todas las pruebas pasadas
- ✅ Documentación exhaustiva
- ✅ Estructura correcta
- ✅ Persistencia verificada
- ✅ Excepciones controladas

**Próximo paso:** Crear repositorio en GitHub y subir archivos

---

**Fecha de preparación:** 2024  
**Estado:** ✅ LISTO PARA ENTREGAR  
**Puntos esperados:** 10/10

---

*Este documento proporciona todas las instrucciones necesarias para una entrega exitosa.*

