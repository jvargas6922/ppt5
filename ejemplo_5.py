"""
formas de poder leer un archivo en python.
    1- Usando read()
    2- Usando readline()
    3- Usando readlines()
"""
import os

ruta_recurso = './archivos/'
archivo_a_leer = ruta_recurso + 'autos.txt' # concatenacion de cadenas.
archivo_a_leer_2 = f"{ruta_recurso}autos.txt" # f-string


with open(archivo_a_leer,'r') as archivo:
    """
        # 1- Usando read()
        contenido = archivo.read() # lee todo el contendo del archivo.
        print("Usando read():")
        print(contenido) # imprime todo el contenido del archivo.
        print(type(contenido)) # str
        # Regreso al inicio del archivo
        # archivo.seek(0) # mueve el cursor al inicio del archivo.
    """

    """
        # 2- Usando readline()
        print("\nUsando readline():")
        linea1 = archivo.readline() # lee la primera linea del archivo.
        print(linea1) # imprime la primera linea del archivo.
        print(type(linea1)) # str
        linea2 = archivo.readline() # lee la segunda linea del archivo.
        print(linea2) # imprime la segunda linea del archivo.
        print(type(linea2)) # str
        # Regreso al inicio del archivo
        # archivo.seek(0)
    """

    # 3- Usando readlines()
    print("\nUsando readlines():")
    lineas = archivo.readlines() # lee todas las lineas del archivo y las guarda en una lista.
    print(lineas) # imprime la lista de lineas del archivo.
    for linea in lineas:
        print(linea) # imprime cada linea del archivo.
    print(type(lineas)) # list