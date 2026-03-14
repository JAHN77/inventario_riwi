# Sistema de Inventario en Python 📦

Este proyecto consiste en un programa básico desarrollado en **Python** que permite registrar productos en un inventario, calcular el costo total de cada producto y mostrar la información almacenada en la consola.

El objetivo del proyecto es aplicar conceptos fundamentales de programación como el uso de **listas, diccionarios, ciclos, validación de datos y entrada de usuario**.

Este repositorio será utilizado para el desarrollo progresivo del sistema durante varias semanas como parte de una actividad académica.

---

## 📖 Descripción del programa

El programa solicita al usuario la cantidad de productos que desea registrar.
Posteriormente, para cada producto se solicita la siguiente información:

* Nombre del producto
* Precio del producto
* Cantidad disponible

El sistema valida los datos ingresados y calcula automáticamente el **costo total** de cada producto utilizando la siguiente operación:

```
costo_total = precio * cantidad
```

Cada producto se almacena dentro de una lista llamada **inventario**, utilizando un **diccionario** para guardar la información.

Finalmente, el programa muestra el inventario completo en la consola.

---
## Diagrama de Flujo

El siguiente diagrama representa el flujo del programa de inventario.

<p align="center">
  <img src="docs\diagrama_flujo_inventario.drawio.png" width="600">
</p>

---

## ⚙️ Funcionalidades actuales

El programa actualmente permite:

* Registrar múltiples productos
* Validar que los datos ingresados sean correctos
* Almacenar los productos en una lista
* Calcular automáticamente el costo total
* Mostrar el inventario completo al finalizar

---

## 🧠 Estructura de datos utilizada

Cada producto se almacena con la siguiente estructura:

```python
producto = {
    "nombre": nombre,
    "precio": precio,
    "cantidad": cantidad,
    "costo_total": precio * cantidad
}
```

Todos los productos se guardan dentro de la lista:

```python
inventario = []
```

---

## 💻 Ejemplo de ejecución

Ejemplo de interacción con el programa:

```
Ingresa la cantidad de productos: 2

------------Producto 1------------
Ingresa nombre del producto: lapiz
Ingresa el precio del producto: 500
Ingrese la cantidad del producto: 3

------------Producto 2------------
Ingresa nombre del producto: cuaderno
Ingresa el precio del producto: 2000
Ingrese la cantidad del producto: 2

===== INVENTARIO =====

------ Producto 1 ------
lapiz:500$
cantidad: 3
costo total: 1500$

------ Producto 2 ------
cuaderno:2000$
cantidad: 2
costo total: 4000$
```

---

## 📋 Requisitos

Para ejecutar el programa es necesario tener instalado:

* **Python 3**

Puedes verificar la instalación con el siguiente comando:

```bash
python --version
```

---

## 🚀 Cómo ejecutar el programa

1. Clonar el repositorio

```bash
git clone https://github.com/JAHN77/inventario_riwi.git
```

2. Entrar en la carpeta del proyecto

```bash
cd inventario_riwi
```

3. Ejecutar el archivo

```bash
python inventario.py
```

---

## 📁 Estructura del proyecto

```
inventario_riwi/
│
├── inventario.py
├── README.md
│
└── docs/
└── diagrama_flujo_inventario.drawio.png
```

---

## 📈 Mejoras futuras

Durante el desarrollo del proyecto se planea agregar nuevas funcionalidades como:

* Mejor validación de datos
* Organización del código utilizando funciones
* Implementación de un menú interactivo
* Posibilidad de buscar productos
* Posible almacenamiento de datos en archivos

---

## 👨‍💻 Autor

**Juan Andres Henriquez Coder Riwi**

**Clan: cortissoz**

