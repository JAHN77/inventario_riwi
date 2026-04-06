import os
import csv


# Función para construir la ruta de la carpeta data
def obtener_ruta_data(nombre_archivo):
    """
    Construye la ruta absoluta hacia la carpeta data.

    Si la carpeta no existe, la crea automáticamente.

    Args:
        nombre_archivo (str): Nombre del archivo a guardar o cargar.

    Returns:
        str: Ruta completa del archivo dentro de data.
    """

    # Obtiene la ruta base del proyecto
    ruta_base = os.path.dirname(os.path.dirname(__file__))

    # Construye la ruta de la carpeta data
    ruta_data = os.path.join(ruta_base, "data")

    # Crea la carpeta si no existe
    os.makedirs(ruta_data, exist_ok=True)

    # Retorna la ruta completa del archivo
    return os.path.join(ruta_data, nombre_archivo)


# Función para guardar el inventario en un archivo CSV
def guardar_csv(inventario, nombre_archivo="inventario.csv", incluir_header=True):
    """
    Guarda el inventario en un archivo CSV dentro de la carpeta data.

    Args:
        inventario (list): Lista de productos.
        nombre_archivo (str): Nombre del archivo CSV.
        incluir_header (bool): Indica si se escribe encabezado.

    Returns:
        None
    """

    # Validación de inventario vacío
    if not inventario:
        print("\033[31mNo hay productos en el inventario para guardar\033[0m\n")
        return

    # Obtener ruta final
    ruta = obtener_ruta_data(nombre_archivo)

    try:
        with open(ruta, mode="w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)

            # Escribir encabezado
            if incluir_header:
                escritor.writerow(["nombre", "precio", "cantidad"])

            # Recorrer inventario y guardar filas
            for producto in inventario:
                escritor.writerow([
                    producto["nombre"],
                    producto["precio"],
                    producto["cantidad"]
                ])

        print(f"\033[32mInventario guardado en: {ruta}\033[0m\n")

    except PermissionError:
        print("\033[31mNo tienes permisos para escribir en el archivo\033[0m\n")

    except Exception as e:
        print(f"\033[31mError al guardar archivo: {e}\033[0m\n")


# Función para cargar inventario desde CSV
def cargar_csv(nombre_archivo="inventario.csv"):
    """
    Carga un inventario desde un archivo CSV dentro de la carpeta data.

    Args:
        nombre_archivo (str): Nombre del archivo CSV.

    Returns:
        tuple: (inventario_cargado, filas_invalidas)
    """

    inventario_cargado = []
    filas_invalidas = 0

    # Obtener ruta final
    ruta = obtener_ruta_data(nombre_archivo)

    try:
        with open(ruta, mode="r", newline="", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)

            # Leer encabezado
            encabezado = next(lector)

            # Validación de encabezado
            if encabezado != ["nombre", "precio", "cantidad"]:
                print("\033[31mEncabezado inválido\033[0m\n")
                return [], 0

            # Leer filas
            for fila in lector:
                try:
                    # Validación cantidad columnas
                    if len(fila) != 3:
                        filas_invalidas += 1
                        continue

                    nombre = fila[0].strip()
                    precio = float(fila[1])
                    cantidad = int(fila[2])

                    # Validación de valores negativos
                    if precio < 0 or cantidad < 0:
                        filas_invalidas += 1
                        continue

                    # Crear producto
                    producto = {
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    }

                    inventario_cargado.append(producto)

                except ValueError:
                    filas_invalidas += 1

        print(
            f"\033[32mArchivo cargado correctamente "
            f"({len(inventario_cargado)} productos)\033[0m"
        )

        if filas_invalidas > 0:
            print(
                f"\033[33m{filas_invalidas} filas inválidas omitidas\033[0m\n"
            )

        return inventario_cargado, filas_invalidas

    except FileNotFoundError:
        print("\033[31mArchivo no encontrado en la carpeta data\033[0m\n")
        return [], 0

    except UnicodeDecodeError:
        print("\033[31mError de codificación del archivo\033[0m\n")
        return [], 0

    except Exception as e:
        print(f"\033[31mError al cargar archivo: {e}\033[0m\n")
        return [], 0