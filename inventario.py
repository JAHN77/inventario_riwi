# inicializa la lista del inventario
inventario = []
validacion_resultado=False

def peticion_datos(mensaje,funcion_validadora):
    
    while True:
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
cantidad_productos = peticion_datos("Ingresa la cantidad de productos que vas a agregar: ", validacion_int)

# registro de productos
for i in range(cantidad_productos):
    
    print(f"\n------------ Producto {i+1} ------------")
    
    # peticion y validación de datos
    nombre=peticion_datos("Ingresa nombre del producto: ", validacion_string)
    precio= peticion_datos("Ingresa el precio del producto: ", validacion_float)
    cantidad=peticion_datos("Ingrese la cantidad del producto: ", validacion_int)
    
    # crear diccionario del producto
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "costo_total": precio * cantidad
    }
    
    # agregar producto al inventario
    inventario.append(producto)


# mostrar inventario
print("\n===== INVENTARIO =====\n")

for i, producto in enumerate(inventario):

    print(f"------ Producto {producto['nombre']} ------")

    print(f"Precio: {producto['precio']}$")
    print(f"Cantidad: {producto['cantidad']}")
    print(f"Costo total: {producto['costo_total']}$\n")

# --------------------------------------------------
# Este programa permite registrar varios productos,
# calcular su costo total (precio * cantidad) y
# mostrar la información almacenada en un inventario.
# --------------------------------------------------