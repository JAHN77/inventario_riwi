# Lista global donde se almacenan los productos del inventario
inventario = []

# Función genérica para solicitar datos al usuario con validación
def peticion_datos(mensaje, funcion_validadora):
    
    # Bucle hasta que el usuario ingrese un valor válido
    while True:
        valor = input(mensaje)
        
        # Se valida el valor con la función recibida
        if funcion_validadora(valor):
            
            # Conversión según el tipo de validación
            if funcion_validadora == validacion_int:
                return int(valor)
            
            if funcion_validadora == validacion_float:
                return float(valor)
                
            # Para strings se limpia espacios
            return valor.strip()


# Validación para números enteros positivos
def validacion_int(numero):
    try:
        numero = int(numero)
        
        if numero > 0:
            return True
        else:
            print("\033[31mLos valores deben ser mayor a 0 \033[0m\n")
            return False
            
    except ValueError:
        print("\033[31m------ Valor incorrecto ------\033[0m\n")
        return False


# Validación para números decimales positivos
def validacion_float(numero):
    try:
        numero = float(numero)
        
        if numero > 0:
            return True
        else:
            print("\033[31mLos valores deben ser mayor a 0 \033[0m\n")
            return False

    except ValueError:
        print("\033[31m------ Valor incorrecto ------\033[0m\n")
        return False


# Validación para cadenas de texto no vacías
def validacion_string(texto):
    try:
        texto = str(texto).strip()
        
        if texto != "":
            return True
        else:
            print("\033[31mLos valores no pueden ser vacios\033[0m\n")
            return False

    except ValueError:
        print("\033[31m------ Valor incorrecto ------\033[0m\n")
        return False


# Función para agregar un producto al inventario
def agregar_producto(nombre, precio, cantidad):
    
    # Se crea el diccionario del producto
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "costo_total": precio * cantidad  # cálculo directo
    }
    
    # Se agrega el producto a la lista global
    inventario.append(producto)

    return inventario


# Función para mostrar todos los productos del inventario
def mostar_inventario(inventario):

    # Validación de inventario vacío
    if not inventario:
        print("\033[31mNo hay productos en el inventario\033[0m\n")
        return
  
    print("\n===== INVENTARIO =====\n")

    # Recorrido del inventario
    for producto in inventario:
        print(f"------ Producto {producto['nombre']} ------")
        print(f"Precio: {producto['precio']}$")
        print(f"Cantidad: {producto['cantidad']}")
        print(f"Costo total: {producto['costo_total']}$\n")


# Función para calcular estadísticas del inventario
def calcular_estadisticas(inventario):

    # Validación de inventario vacío
    if not inventario:
        print("\033[31mNo hay productos en el inventario\033[0m\n")
        return

    print("\n===== ESTADÍSTICAS DEL INVENTARIO =====\n")

    # Total de unidades (sumatoria de cantidades)
    total_unidades = sum(producto['cantidad'] for producto in inventario)

    # Número de tipos de productos
    total_tipos = len(inventario)

    # Valor total del inventario (precio * cantidad)
    valor_total = sum(producto['precio'] * producto['cantidad'] for producto in inventario)

    # Mostrar resultados
    print(f"Tipos de productos registrados: {total_tipos}")
    print(f"Total de unidades en inventario: {total_unidades}")
    print(f"Valor total del inventario: ${valor_total:.2f}\n")


# Función principal que controla el menú interactivo
def menu():
    
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
                
                agregar_producto(nombre, precio, cantidad)
                print("\033[32mProducto agregado correctamente\033[0m\n")

            # Opción 2: mostrar inventario
            case "2":
                mostar_inventario(inventario)

            # Opción 3: calcular estadísticas
            case "3":
                calcular_estadisticas(inventario)

            # Opción 4: salir del programa
            case "4":
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