# inicializa la lista del inventario
inventario = []
validacion_resultado=False

def peticion_datos(mensaje,funcion_validadora,validador):
    
    while validador==False:
        valor = input(mensaje)
        
        if funcion_validadora(valor):
            
            if funcion_validadora==validacion_int:
                return int(valor)
            
            if funcion_validadora==validacion_float:
                return float(valor)
                
            return valor.strip()

def validacion_int(numero):
    try:
        
        numero=int(numero)
        
        if numero> 0:
            
            return True
            
        else:
            
            print("\033[31mLos valores deben ser mayor a 0 \033[0m\n")
            return False
            
    except ValueError:
        
        print("\033[31m------ Valor incorrecto ------\033[0m\n")
        return False

def validacion_float(numero):
    try:
        numero=float(numero)
        
        if numero> 0:
            
            return True
            
        else:
            
            print("\033[31mLos valores deben ser mayor a 0 \033[0m\n")
            return False

    except ValueError:
        
        print("\033[31m------ Valor incorrecto ------\033[0m\n")
        return False

def validacion_string(texto):
    try:
        texto=str(texto).strip()
        
        if texto != "":
            
            return True
            
        else:
            
            print("\033[31mLos valores no pueden ser vacios\033[0m\n")
            return False

    except ValueError:
        
        print("\033[31m------ Valor incorrecto ------\033[0m\n")
        return False





# petición de cantidad de productos
    
cantidad_productos = peticion_datos("Ingresa la cantidad de productos que vas a agregar: ", validacion_int,validacion_resultado)

# registro de productos
for i in range(cantidad_productos):

    while validacion_resultado==False:

        print(f"\n------------ Producto {i+1} ------------")

        nombre = input("Ingresa nombre del producto: ")
        precio = input("Ingresa el precio del producto: ")
        cantidad = input("Ingrese la cantidad del producto: ")

        # validación de datos
        if nombre.isalpha() and precio.isdigit() and cantidad.isdigit():

            precio = float(precio)
            cantidad = int(cantidad)

            if precio > 0 and cantidad > 0:

                print("\033[32mDatos ingresados correctamente\033[0m\n")

                # crear diccionario del producto
                producto = {
                    "nombre": nombre,
                    "precio": precio,
                    "cantidad": cantidad,
                    "costo_total": precio * cantidad
                }

                break

        else:
            print("\033[31m------ Tipo de valores incorrectos ------\033[0m\n")

    # agregar producto al inventario
    inventario.append(producto)


# mostrar inventario
print("\n===== INVENTARIO =====\n")

for i, producto in enumerate(inventario):

    print(f"------ Producto {i+1} ------")

    print(f"{producto['nombre']}: {producto['precio']}$")
    print(f"Cantidad: {producto['cantidad']}")
    print(f"Costo total: {producto['costo_total']}$\n")


# --------------------------------------------------
# Este programa permite registrar varios productos,
# calcular su costo total (precio * cantidad) y
# mostrar la información almacenada en un inventario.
# --------------------------------------------------