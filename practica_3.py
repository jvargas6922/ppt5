"""
Contexto: 🙌
Estás creando una herramienta que permita a los usuarios inspeccionar archivos locales. 
El objetivo es obtener información del archivo y mostrar su contenido de manera distinta según su tamaño, 
usando buenas prácticas de manejo de archivos en Python.
Consigna: ✍
● Implementá un programa en Python que:
    ○ Solicite al usuario el nombre de un archivo (listo)
    ○ Abra el archivo en modo lectura ("r") (listo)
    ○ Obtenga y muestre:
        ■ Nombre del archivo (.name) (listo)
        ■ Modo de apertura (.mode) (listo)
        ■ Estado de cierre (.closed) (listo)
        ■ Tamaño en bytes usando os.stat() (listo)
    ○ Lea el contenido:
        ■ Si el archivo pesa menos de 500 bytes →
    leé todo el contenido con read()
        ■ Si pesa más de 500 bytes → leé línea por
    línea con readline()
● Asegurate de cerrar el archivo y mostrar que fue cerrado correctamente
● Usá try/except para manejar errores si el archivo no existe
"""
import os 

# ruta del recurso.
ruta_recurso = './archivos/'
archivo = ruta_recurso + "autos.txt"

# verificar si el archivo existe en la ruta 
# if not os.path.exists(archivo):
#     print(f"Error: La ruta '{ruta_recurso}' no existe.")
# else:
#     print(f"La ruta '{ruta_recurso}' existe.")

# abrir con with para asegurarnos que al terminar se cierre el archivo
# la otra forma es con open y luego close

data = open(archivo, "r")
try:
    print(f"Nombre del archivo : {data.name}") # nombre del archivo
    print(f"Modo de apertura : {data.mode}") # modo de apertura
    print(f"Estado de cierre : {data.closed}") # estado de cierre
    print(f"Tamaño en bytes : {os.stat(archivo).st_size}") # tamaño en bytes
    # tamaño del archivo
    size = os.stat(archivo).st_size

    if size < 500:
        contenido = data.read()
        print(contenido)
    else:
        for linea in data:
            print(linea.strip()) # .strip() para eliminar saltos de línea adicionales

    data.close() # cierrar el archivo
    print(f"Estado de cierre después de cerrar el archivo : {data.closed}") # estado
except:
    print("Error al procesar data")
