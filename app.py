"""
Manejo de archivos en python

Modos de apertura:
- 'r'  : Modo lectura. "El archivo debe existir".
- 'w'  : Modo escritura. Crea un archivo nuevo o sobrescribe uno existente.
- 'a'  : Modo anexar. Añade contenido al final del archivo existente o crea uno nuevo.
- 'r+' : Modo lectura y escritura. El archivo debe existir.
- 'b'  : Modo binario. Se puede combinar con otros modos (ejemplo: 'rb', 'wb').

Operaciones basicas sobre un archivo:
- Abrir
    Ejemplo:
    with open('nombre_archivo.extension', 'r') as archivo:
        contenido = archivo.read()
    
    Traduccion del codigo anterior:
        abrimos el archivo 'nombre_archivo.extension' en modo lectura ('r')
        y lo asignamos a la variable 'archivo'.
        El bloque 'with' asegura que el archivo se cierre correctamente despues de su uso.
 ----------------------------------------------
- Leer
    Ejemplo:
    with open('nombre_archivo.extension', 'r') as archivo:
        contenido = archivo.read()
        print(contenido)
 ----------------------------------------------
- Escribir
    Ejemplo:
    with open('nombre_archivo.extension', 'w') as archivo:
        archivo.write('Este es un nuevo contenido.')

    Traduccion del codigo anterior:
        abrimos el archivo 'nombre_archivo.extension' en modo escritura ('w')
        y escribimos 'Este es un nuevo contenido.' en el archivo.
 ----------------------------------------------
- Modificar
    Ejemplo:
    with open('nombre_archivo.extension', 'a') as archivo:
        archivo.write('\nEste es un contenido adicional.')

    Traduccion del codigo anterior:
        abrimos el archivo 'nombre_archivo.extension' en modo anexar ('a')
        y añadimos 'Este es un contenido adicional.' al final del archivo.
 ----------------------------------------------
- Cerrar
    Ejemplo:
    archivo = open('nombre_archivo.extension', 'r')
    contenido = archivo.read()
    archivo.close()

    Traduccion del codigo anterior:
        abrimos el archivo 'nombre_archivo.extension' en modo lectura ('r'),
        leemos su contenido y luego cerramos el archivo para liberar recursos.
"""