from servicios import *

# Función principal que controla el menú interactivo
def menu():
    # Lista global donde se almacenan los productos del inventario
    inventario = []

    # Bucle infinito hasta que el usuario decida salir
    while True:
        print("\n===== MENÚ INVENTARIO =====")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Calcular estadísticas")
        print("4. Salir")

        # Captura de opción
        opcion = input("Seleccione una opción: ").strip()

        # Estructura de control usando match-case (Python 3.10+)
        match opcion:

            # Opción 1: agregar producto
            case "1":
                print("\n--- Agregar Producto ---")
                
                nombre = peticion_datos("Ingresa nombre del producto: ", validacion_string)
                precio = peticion_datos("Ingresa el precio del producto: ", validacion_float)
                cantidad = peticion_datos("Ingrese la cantidad del producto: ", validacion_int)
                
                agregar_producto(inventario,nombre, precio, cantidad)
                print("\033[32mProducto agregado correctamente\033[0m\n")

            # Opción 2: mostrar inventario
            case "2":
                mostar_inventario(inventario)
            
            # Opción 3: Buscar producto
            case "3":
                buscar_producto(inventario)

            # Opción 4: Actualzar producto
            case "4":
                print("")

            # Opción 5: Eliminar producto
            case "5":
                print("")

            # Opción 6: calcular estadísticas
            case "6":
                calcular_estadisticas(inventario)
            
            # Opción 7: Guardar inventario CSV
            case "7":
                print("")
            
            # Opción 8: Cargar inventario CSV
            case "8":
                print("")

            # Opción 9: salir del programa
            case "9":
                print("\nSaliendo del sistema... 👋")
                break

            # Manejo de opción inválida
            case _:
                print("\033[31mOpción inválida, intenta nuevamente\033[0m\n")



# Punto de entrada del programa
menu()

# --------------------------------------------------
# Este programa permite:
# - Registrar productos en un inventario
# - Validar datos ingresados por el usuario
# - Mostrar los productos almacenados
# - Calcular estadísticas básicas del inventario
# Utiliza estructuras de control, listas y diccionarios.
# --------------------------------------------------