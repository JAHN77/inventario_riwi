import os
from servicios import *
from archivos import *


# -----------------UTILIDADES VISUALES-----------------

# Colores
ROJO = "\033[31m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"
AZUL = "\033[34m"
CYAN = "\033[36m"
RESET = "\033[0m"


# Función para limpiar terminal
def limpiar_terminal():
    """
    Limpia la pantalla de la terminal.
    """
    os.system("cls" if os.name == "nt" else "clear")


# Función para pausar la terminal
def pausar():
    """
    Pausa la ejecución hasta que el usuario presione Enter.
    """
    input(f"\n{AMARILLO}Presiona Enter para continuar...{RESET}")


# Función para imprimir títulos
def imprimir_titulo(texto):
    """
    Muestra un título destacado en consola.
    """
    print(f"\n{CYAN}{'=' * 45}")
    print(f"{texto.center(45)}")
    print(f"{'=' * 45}{RESET}\n")


# Función principal que controla el menú interactivo
def menu():
    """
    Controla el menú principal del sistema de inventario.
    """

    # Lista donde se almacenan los productos
    inventario = []

    while True:
        limpiar_terminal()

        imprimir_titulo("SISTEMA DE GESTIÓN DE INVENTARIO")

        print(f"{AZUL}1.{RESET} Agregar producto")
        print(f"{AZUL}2.{RESET} Mostrar inventario")
        print(f"{AZUL}3.{RESET} Buscar producto")
        print(f"{AZUL}4.{RESET} Actualizar producto")
        print(f"{AZUL}5.{RESET} Eliminar producto")
        print(f"{AZUL}6.{RESET} Calcular estadísticas")
        print(f"{AZUL}7.{RESET} Guardar inventario CSV")
        print(f"{AZUL}8.{RESET} Cargar inventario CSV")
        print(f"{ROJO}9.{RESET} Salir")

        opcion = input("\nSeleccione una opción: ").strip()

        match opcion:

            # Opción 1
            case "1":
                limpiar_terminal()
                imprimir_titulo("AGREGAR PRODUCTO")

                nombre = peticion_datos(
                    "Ingresa nombre del producto: ",
                    validacion_string
                )

                precio = peticion_datos(
                    "Ingresa el precio del producto: ",
                    validacion_float
                )

                cantidad = peticion_datos(
                    "Ingresa la cantidad del producto: ",
                    validacion_int
                )

                producto = agregar_producto(
                    inventario,
                    nombre,
                    precio,
                    cantidad
                )

                if producto is not None:
                    print(
                        f"{VERDE}Producto '{nombre}' agregado correctamente{RESET}"
                    )
                else:
                    print(
                        f"{ROJO}El producto '{nombre}' ya existe{RESET}"
                    )

                pausar()

            # Opción 2
            case "2":
                limpiar_terminal()
                imprimir_titulo("INVENTARIO")
                mostrar_inventario(inventario)
                pausar()

            # Opción 3
            case "3":
                limpiar_terminal()
                imprimir_titulo("BUSCAR PRODUCTO")

                nombre = peticion_datos(
                    "Ingresa el nombre del producto: ",
                    validacion_string
                )

                producto = buscar_producto(inventario, nombre)

                if producto:
                    subtotal = (
                        producto["precio"] * producto["cantidad"]
                    )

                    print(f"{VERDE}Producto encontrado:{RESET}\n")
                    print(f"Nombre: {producto['nombre']}")
                    print(f"Precio: ${producto['precio']}")
                    print(f"Cantidad: {producto['cantidad']}")
                    print(f"Subtotal: ${subtotal}")

                else:
                    print(f"{ROJO}Producto no encontrado{RESET}")

                pausar()

            # Opción 4
            case "4":
                limpiar_terminal()
                imprimir_titulo("ACTUALIZAR PRODUCTO")

                nombre = peticion_datos(
                    "Ingresa el nombre del producto: ",
                    validacion_string
                )

                nuevo_precio = peticion_datos(
                    "Nuevo precio: ",
                    validacion_float
                )

                nueva_cantidad = peticion_datos(
                    "Nueva cantidad: ",
                    validacion_int
                )

                actualizar_producto(inventario,nombre,nuevo_precio,nueva_cantidad)

                pausar()

            # Opción 5
            case "5":
                limpiar_terminal()
                imprimir_titulo("ELIMINAR PRODUCTO")

                nombre = peticion_datos(
                    "Ingresa el nombre del producto: ",
                    validacion_string
                )

                producto = eliminar_producto(inventario, nombre)

                if producto:
                    print(
                        f"{VERDE}Producto eliminado correctamente{RESET}"
                    )
                else:
                    print(
                        f"{ROJO}Producto no encontrado{RESET}"
                    )

                pausar()

            # Opción 6
            case "6":
                limpiar_terminal()
                imprimir_titulo("ESTADÍSTICAS")
                calcular_estadisticas(inventario)
                pausar()

            # Opción 7
            case "7":
                limpiar_terminal()
                imprimir_titulo("GUARDAR INVENTARIO")

                guardar_csv(inventario)

                pausar()

            # Opción 8
            case "8":
                limpiar_terminal()
                imprimir_titulo("CARGAR INVENTARIO")

                inventario_cargado, filas_invalidas = cargar_csv()

                if inventario_cargado:
                    accion = input(
                        "¿Sobrescribir inventario actual? (S/N): "
                    ).strip().upper()

                    if accion == "S":
                        inventario = inventario_cargado
                        print(
                            f"{VERDE}Inventario reemplazado correctamente{RESET}"
                        )

                    elif accion == "N":
                        for producto_nuevo in inventario_cargado:
                            producto_existente = buscar_producto(
                                inventario,
                                producto_nuevo["nombre"]
                            )

                            if producto_existente:
                                producto_existente["cantidad"] += (
                                    producto_nuevo["cantidad"]
                                )
                                producto_existente["precio"] = (
                                    producto_nuevo["precio"]
                                )
                            else:
                                inventario.append(producto_nuevo)

                        print(
                            f"{VERDE}Inventario fusionado correctamente{RESET}"
                        )

                    print(
                        f"{AMARILLO}Filas inválidas: {filas_invalidas}{RESET}"
                    )

                pausar()

            # Opción 9
            case "9":
                limpiar_terminal()
                print(f"{VERDE}Saliendo del sistema... {RESET}")
                break

            # Opción inválida
            case _:
                print(f"{ROJO}Opción inválida{RESET}")
                pausar()


# Punto de entrada
menu()

# --------------------------------------------------
# SISTEMA DE GESTIÓN DE INVENTARIO
# --------------------------------------------------
# Este programa permite administrar un inventario de
# productos mediante operaciones CRUD:
# - Agregar productos
# - Mostrar inventario
# - Buscar productos
# - Actualizar productos
# - Eliminar productos
#
# Además, incluye:
# - Validación de datos ingresados por el usuario
# - Cálculo de estadísticas del inventario
# - Persistencia de datos en archivos CSV
#   (guardar y cargar información)
#
# El sistema utiliza estructuras de control, listas,
# diccionarios, módulos y manejo de archivos para
# garantizar una solución modular, organizada y
# persistente.
# --------------------------------------------------