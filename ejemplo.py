"""
Diseñe un programa en python que me permita leer un serie de nombres desde un archivo txt.
"""
import os

# saber la ruta donde tengo el archivo txt
# ruta absoluta del archivo
# ruta_archivo = '/Users/joffredvargas/Desktop/PPT5/archivos/nombres_ejemplo.txt'
# ruta relativa del archivo
ruta_archivo = './archivos/nombres_ejemplo.txt'
nombres = []
# validar la ruta del recurso.
if not os.path.exists(ruta_archivo):
    print(f"Error: La ruta '{ruta_archivo}' no existe.")
else:
    print(f"La ruta '{ruta_archivo}' es valida.")
    # apertura de archivo en modo lectura.
    try:
        with open(ruta_archivo, 'r') as archivo:
            contenido = archivo.read()
            # quiero saber el tipo de dato de la variable contenido.
            # print(type(contenido))
            nombres = contenido.splitlines()
            print(nombres)
        # print(contenido)
    except FileNotFoundError:
        print(f"Error: El archivo en la ruta '{ruta_archivo}' no fue encontrado.")