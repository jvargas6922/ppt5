"""
    Diseñe un programa en python que me permita escribir un archivo con una serie de nombres desde un archivo txt.
"""
import os

ruta_recursos = './archivos/'
autos = ['Toyota', 'Mazda', 'Hyundai', 'Kia', 'Chevrolet', 'Ford', 'Renault', 'Volkswagen', 'Nissan', 'Honda']


with open(ruta_recursos + 'autos.txt', 'w') as archivo:
        for auto in autos:
            archivo.write(auto + '\n')
print(f"Archivo 'autos.txt' creado en la ruta '{ruta_recursos}' con los nombres de autos.")