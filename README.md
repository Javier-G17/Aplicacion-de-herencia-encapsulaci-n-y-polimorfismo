# Sistema de Gestión de Restaurante

## Información del estudiante

*Nombre:* Bonner Javier García Guanga.

## Descripción del sistema

Este proyecto consiste en un sistema básico de gestión de restaurante desarrollado en Python utilizando Programación Orientada a Objetos (POO). El sistema permite registrar y visualizar productos del restaurante mediante el uso de herencia, encapsulación y polimorfismo.

Los productos se clasifican en dos categorías: platillos y bebidas. Cada producto almacena información como nombre, precio y disponibilidad, mientras que las clases especializadas agregan características propias de cada tipo de producto.

## Estructura del proyecto

```text
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── platillo.py
│   └── bebida.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py
```

### Descripción de los archivos

- *modelos/producto.py:* Contiene la clase padre Producto, donde se definen los atributos y métodos comunes de todos los productos.
- *modelos/platillo.py:* Contiene la clase Platillo, que hereda de Producto y agrega el atributo calorias.
- *modelos/bebida.py:* Contiene la clase Bebida, que hereda de Producto y agrega el atributo volumen_ml.
- *servicios/restaurante.py:* Contiene la clase Restaurante, encargada de administrar la lista de productos registrados.
- *main.py:* Es el punto de entrada del programa. Permite registrar productos desde la consola y mostrar la información almacenada.

## Relación de herencia aplicada

La herencia implementada en el proyecto es la siguiente:

```text
Producto
├── Platillo
└── Bebida
```
La clase Producto funciona como clase padre y proporciona atributos y métodos comunes. Las clases Platillo y Bebida heredan estas características y añaden información específica para cada tipo de producto.

## Atributo encapsulado

Para aplicar el principio de encapsulación se utilizó el atributo privado:

```python
__precio
```
Este atributo no puede ser modificado directamente desde otras clases. Para acceder o modificar su valor se utilizan los métodos:

```python
obtener_precio()
cambiar_precio()
```
Además, el método cambiar_precio() valida que el nuevo precio sea mayor que cero antes de realizar la modificación.

## Método utilizado para demostrar polimorfismo

El polimorfismo se demuestra mediante el método:

```python
mostrar_informacion()
```

Este método está definido en la clase Producto y es sobrescrito en las clases Platillo y Bebida.

Cuando la clase Restaurante recorre la lista de productos y ejecuta:

```python
producto.mostrar_informacion()
```

cada objeto ejecuta su propia versión del método, mostrando información diferente según el tipo de producto.

## Reflexión

La Programación Orientada a Objetos permite desarrollar sistemas más organizados, reutilizables y fáciles de mantener. La aplicación de principios como herencia, encapsulación y polimorfismo ayuda a reducir la duplicación de código y facilita futuras mejoras del software. Además, la organización modular del proyecto mejora la claridad del código y permite separar responsabilidades de manera adecuada.