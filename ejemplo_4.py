"""
    Diseñe un programa en python que me permita leer un serie de nombres desde un archivo txt.
"""
import os

# ruta del recurso
ruta_recursos = './archivos/'
archivo = ruta_recursos + 'nombres_ejemplo.txt'

archivo_lectura = open(archivo, 'r')
contenido = archivo_lectura.read()
print(contenido)
archivo_lectura.close()
