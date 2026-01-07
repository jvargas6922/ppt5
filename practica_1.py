"""
¿En qué consistirá la Demo?
Vas a abrir un archivo de texto en modo lectura, leer todo su contenido y luego cerrarlo manualmente.
1. Usar open() en modo "r" para abrir un archivo llamado "prueba.txt"
2. Leer el contenido usando read()
3. Imprimir el contenido en consola
4. Cerrar el archivo usando close()
🔹 Observaciones importantes:
    ➢ Si el archivo no existe, Python lanzará un FileNotFoundError
    ➢ Verificar si el archivo realmente se cerró con archivo.closed
"""
import os

ruta_recursos = './archivos/'
try:
    # abrir el archivo en modo lectura
    archivo = open(ruta_recursos + 'autos.txt', 'r')
    # leer el contenido del archivo
    contenido = archivo.read()
    # imprimir el contenido en consola
    print(contenido)
    # cerrar el archivo
    archivo.close() # True
    # verificar si el archivo se cerró
    if archivo.closed:
        print("El archivo se cerró correctamente.")
except FileNotFoundError:
    print(f"Error: El archivo en la ruta '{ruta_recursos + 'prueba.txt'}' no fue encontrado.")