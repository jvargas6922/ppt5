"""
Crea un proyecto que te permita simular una ataque por fuerza bruta 
y 
saber si la contraseña creada es fuerte o débil.
"""
import os

password = input("Crea la contraseña a evaluar: ")
intentos = 0
encontrada = False # bandera para indicar si se encontró la contraseña (flag)
ruta = './archivos/'
nombre_archivo = "rockyou.txt"

with open(ruta + nombre_archivo, "r", encoding="latin-1") as archivo:
    try:
        for linea in archivo:
            intentos += 1
            if linea.strip() == password:
                print(f"Contraseña encontrada: {password} en {intentos} intentos.")
                encontrada = True
                break
            else:
                if intentos % 100000 == 0:
                    print(f"{intentos} intentos realizados...")
                    break

            # if not encontrada:
            #     print("Contraseña no encontrada en el diccionario. La contraseña es fuerte.")
            #     break
    except KeyboardInterrupt:
        print("\nProceso interrumpido por el usuario.")
    