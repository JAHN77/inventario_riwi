# Función genérica para solicitar datos al usuario con validación
def peticion_datos(mensaje, funcion_validadora):
    """
    Solicita un dato al usuario y lo valida usando una función validadora.

    Args:
        mensaje (str): Texto mostrado al usuario.
        funcion_validadora (function): Función encargada de validar.

    Returns:
        int | float | str: Valor convertido según el tipo.
    """

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
    """
    Valida que el número sea entero y mayor a cero.
    """
    try:
        numero = int(numero)

        if numero > 0:
            return True
        else:
            print("\033[31mLos valores deben ser mayores a 0\033[0m\n")
            return False

    except ValueError:
        print("\033[31mValor incorrecto\033[0m\n")
        return False


# Validación para números decimales positivos
def validacion_float(numero):
    """
    Valida que el número sea decimal y mayor a cero.
    """
    try:
        numero = float(numero)

        if numero > 0:
            return True
        else:
            print("\033[31mLos valores deben ser mayores a 0\033[0m\n")
            return False

    except ValueError:
        print("\033[31mValor incorrecto\033[0m\n")
        return False


# Validación para cadenas de texto no vacías
def validacion_string(texto):
    """
    Valida que el texto no esté vacío.
    """
    try:
        texto = str(texto).strip()

        if texto != "":
            return True
        else:
            print("\033[31mEl texto no puede estar vacío\033[0m\n")
            return False

    except ValueError:
        print("\033[31mValor incorrecto\033[0m\n")
        return False


# -----------------FUNCIONES-----------------

# Función para agregar un producto al inventario
def agregar_producto(inventario, nombre, precio, cantidad):
    """
    Agrega un producto al inventario.

    Returns:
        dict | None: Producto agregado o None si ya existe.
    """

    producto_existente = buscar_producto(inventario, nombre)

    if producto_existente is not None:
        return None

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)

    return producto

# Función para mostrar todos los productos del inventario
def mostrar_inventario(inventario):
    """
    Muestra todos los productos del inventario.
    """

    # Validación de inventario vacío
    if not inventario:
        print("\033[31mNo hay productos en el inventario\033[0m\n")
        return

    # Encabezados
    print(
        f"{'Nombre':<20}"
        f"{'Precio':<15}"
        f"{'Cantidad':<15}"
        f"{'Subtotal':<15}"
    )

    print("-" * 65)

    # Recorrido del inventario
    for producto in inventario:
        costo_total = (
            producto["precio"] * producto["cantidad"]
        )

        print(
            f"{producto['nombre']:<20}"
            f"${producto['precio']:<14.2f}"
            f"{producto['cantidad']:<15}"
            f"${costo_total:<14.2f}"
        )

    print()


# Función para buscar producto
def buscar_producto(inventario, nombre):
    """
    Busca un producto por nombre.
    """

    for producto in inventario:
        if nombre.lower() == producto["nombre"].lower():
            return producto

    return None


# Función para actualizar un producto del inventario
def actualizar_producto(inventario,nombre,nuevo_precio=None,nueva_cantidad=None):
    """
    Actualiza un producto existente.

    Returns:
        dict | None: Producto actualizado o None.
    """

    producto = buscar_producto(inventario, nombre)

    if producto is None:
        return None

    if nuevo_precio is not None:
        producto["precio"] = nuevo_precio

    if nueva_cantidad is not None:
        producto["cantidad"] = nueva_cantidad

    return producto


# Función para eliminar un producto del inventario
def eliminar_producto(inventario, nombre):
    """
    Elimina un producto del inventario.

    Returns:
        dict | None: Producto eliminado o None.
    """

    producto = buscar_producto(inventario, nombre)

    if producto is None:
        return None

    inventario.remove(producto)

    return producto


# Función para calcular estadísticas del inventario
def calcular_estadisticas(inventario):
    """
    Calcula y muestra estadísticas generales.
    """

    if not inventario:
        print("\033[31mNo hay productos en el inventario\033[0m\n")
        return

    total_unidades = sum(
        producto["cantidad"] for producto in inventario
    )

    total_tipos = len(inventario)

    valor_total = sum(
        producto["precio"] * producto["cantidad"]
        for producto in inventario
    )

    producto_mas_caro = max(
        inventario,
        key=lambda producto: producto["precio"]
    )

    producto_mayor_stock = max(
        inventario,
        key=lambda producto: producto["cantidad"]
    )

    print(f"Tipos registrados      : {total_tipos}")
    print(f"Total unidades         : {total_unidades}")
    print(f"Valor total            : ${valor_total:.2f}")

    print(
        f"Producto más caro      : "
        f"{producto_mas_caro['nombre']} "
        f"(${producto_mas_caro['precio']:.2f})"
    )

    print(
        f"Mayor stock            : "
        f"{producto_mayor_stock['nombre']} "
        f"({producto_mayor_stock['cantidad']} unidades)"
    )

    print()