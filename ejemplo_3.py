"""
    Diseñe un programa en python que me permita anexar mas informacion al archivo existente el nombre del archivo es autos.txt.
"""
import os

ruta_recursos = './archivos/'
frutas = ['Manzana', 'Banana', 'Cereza', 'Durazno', 'Uva', 'Pera', 'Piña', 'Mango', 'Kiwi', 'Fresa']

with open(ruta_recursos + 'autos.txt', 'a') as archivo:
        for fruta in frutas:
            archivo.write(fruta + '\n')
print(f"Información adicional de frutas anexada al archivo 'autos.txt' en la ruta '{ruta_recursos}'.")