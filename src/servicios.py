
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

# -----------------VALIDACIONES-----------------

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

#-----------------FUNCIONES-----------------

# Función para agregar un producto al inventario
def agregar_producto(inventario,nombre, precio, cantidad):
    
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

#Funcion para buscar 
def buscar_producto(inventario):
    try:

        for producto in inventario:

            producto_buscar=input("ingresa el nombre a buscar: ")

            if producto_buscar.lower() == producto["nombre"].lower():

                print("si se encuentra")
                print(producto)
    except:
        print("producto no encontrado")

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


