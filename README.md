# Semana 10 - Persistencia de Productos con JSON

Este directorio contiene la evolución del proyecto **restaurante_app** para la Semana 10, incorporando persistencia de productos mediante archivos JSON.

## Contenido

- **restaurante_app/**: Proyecto completo con arquitectura modular
  - `main.py`: Punto de entrada
  - `modelos/`: Clases de dominio (Producto, Bebida, Usuario)
  - `servicios/`: Servicios de negocio (Restaurante, ArchivoServicio)
  - `datos/`: Directorio para almacenamiento JSON
  - `README.md`: Documentación detallada

## Inicio Rápido

```bash
python restaurante_app/main.py
```

## Características Principales

✅ Persistencia automática de productos en JSON  
✅ Carga de productos al iniciar el programa  
✅ Manejo robusto de excepciones  
✅ Arquitectura modular y escalable  
✅ Soporte para Producto y Bebida  
✅ Interfaz de menú interactiva  

## Documentación

Consultar `restaurante_app/README.md` para información detallada sobre:
- Estructura del proyecto
- Funcionamiento de la persistencia
- Flujos de carga y guardado
- Manejo de excepciones
- Instrucciones de ejecución
- Pruebas de validación

## Mejoras de la Semana 10

1. **Nuevo servicio ArchivoServicio** para manejo centralizado de JSON
2. **Método a_diccionario()** en Producto y Bebida
3. **Carga automática** de productos al iniciar
4. **Guardado automático** después de operaciones de modificación
5. **Excepciones específicas** controladas para archivos y datos
6. **Validación robusta** de registros JSON incompletos o inválidos

## Requisitos

- Python 3.8 o superior
- Solo módulos estándar (json, os, typing, re)

## Autor

[Tu nombre completo]

---

*Proyecto desarrollado para la Semana 10, Parcial 2*

