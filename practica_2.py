"""
¿En qué consistirá la Demo?
Vas a abrir un archivo de texto y leerlo usando los tres métodos principales, observando qué devuelve cada uno.
1. Abrí el archivo "prueba.txt" en modo lectura ("r")
2. Probá cada método por separado: read(), readline() y readlines()
"""
import os 

ruta_recurso = './archivos/'
archivo_a_leer = ruta_recurso + 'nombres_ejemplo.txt' # concatenacion de cadenas.
archivo_a_leer_2 = f"{ruta_recurso}nombres_ejemplo.txt" # f-string


with open(archivo_a_leer,'r') as archivo:
    
    # 1- Usando read()
    # contenido = archivo.read() # lee todo el contendo del archivo.
    # print("Usando read():")
    # print(contenido) # imprime todo el contenido del archivo.
    # print(type(contenido)) # str
    # # Regreso al inicio del archivo
    # # archivo.seek(0) # mueve el cursor al inicio del archivo.
    

    
    # 2- Usando readline()
    # print("\nUsando readline():")
    # linea1 = archivo.readline() # lee la primera linea del archivo.
    # print(linea1) # imprime la primera linea del archivo.
    # print(type(linea1)) # str
    # linea2 = archivo.readline() # lee la segunda linea del archivo.
    # print(linea2) # imprime la segunda linea del archivo.
    # print(type(linea2)) # str
    # # Regreso al inicio del archivo
    # # archivo.seek(0)
    

    # 3- Usando readlines()
    print("\nUsando readlines():")
    lineas = archivo.readlines() # lee todas las lineas del archivo y las guarda en una lista.
    print(lineas) # imprime la lista de lineas del archivo.
    for linea in lineas:
        print(linea) # imprime cada linea del archivo.
    print(type(lineas)) # list
