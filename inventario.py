# inicializa la lista del inventario
inventario = []

# petición de cantidad de productos
while True:
    cantidad_productos = input("Ingresa la cantidad de productos: ")

    if cantidad_productos.isdigit():
        cantidad_productos = int(cantidad_productos)
        break
    else:
        print("\033[31m------ Valor incorrecto ------\033[0m\n")


# registro de productos
for i in range(cantidad_productos):

    while True:

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