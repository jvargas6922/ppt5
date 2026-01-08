"""
crea un programa que simule las operacion de compra en un minimarket.
    - Compra de una fruta
    - Compra de una verdura
    - Compra de un snack
    - Compra de una bebida
"""
import os
# Recursos del desarrollo
frutas = ["manzana", "banana", "naranja", "pera"]
verduras = ["lechuga", "tomate", "zanahoria", "pepino"]
snacks = ["papas fritas", "galletas", "chocolates", "frutos secos"]
bebidas = ["agua", "jugo", "refresco", "cerveza"]
ruta_archivos = './archivos/'
nombre_archivo = "compras_minimarket.txt"
archivo = ruta_archivos + nombre_archivo

# estructuras necesarias para la version -> V2
mensaje_bienvenida = "Bienvenido al minimarket, ¿qué desea comprar?"

data = open(archivo, "a")
opciones_menu = ["1. Fruta", "2. Verdura", "3. Snack", "4. Bebida", "5. Salir"]

#V1
# while True:
#     print("Bienvenido al minimarket, ¿qué desea comprar?")
#     print("1. Fruta")
#     print("2. Verdura")
#     print("3. Snack")
#     print("4. Bebida")
#     print("5. Salir")

#     # opciones a escojer
#     opcion = input("Ingrese el número de la opción deseada: ")
#     # opcion => str

#     if opcion == "1":
#         print("las frutas disponibles son:")
#         for fruta in frutas:
#             print(f"- {fruta}")
#         eleccion = input("¿Qué fruta desea comprar? ")
#         if eleccion in frutas:
#             try:
#                 print(f"Ha comprado una {eleccion}. ¡Gracias por su compra!")
#                 mensaje = f"Ha comprado una {eleccion}. ¡Gracias por su compra!"
#                 data.write(mensaje + "\n")
#             except Exception as e:
#                 print(e)
#                 print("Error al escribir en el archivo.")
#         else:
#             print("Lo siento, esa fruta no está disponible.")
#     elif opcion == "2":
#         print("las verduras disponibles son:")
#         for verdura in verduras:
#             print(f"- {verdura}")
#         eleccion = input("¿Qué verdura desea comprar? ")
#         if eleccion in verduras:
#             try:
#                 print(f"Ha comprado una {eleccion}. ¡Gracias por su compra!")
#                 mensaje = f"Ha comprado una {eleccion}. ¡Gracias por su compra!"
#                 data.write(mensaje + "\n")
#             except Exception as e:
#                 print(e)
#                 print("Error al escribir en el archivo.")
#         else:
#             print("Lo siento, esa verdura no está disponible.")
#     elif opcion == "3":
#         print("los snacks disponibles son:")
#         for snack in snacks:
#             print(f"- {snack}")
#         eleccion = input("¿Qué snack desea comprar? ")
#         if eleccion in snacks:
#             try:
#                 print(f"Ha comprado un paquete de {eleccion}. ¡Gracias por su compra!")
#                 mensaje = f"Ha comprado un paquete de {eleccion}. ¡Gracias por su compra!"
#                 data.write(mensaje + "\n")
#             except Exception as e:
#                 print(e)
#                 print("Error al escribir en el archivo.")
#         else:
#             print("Lo siento, ese snack no está disponible.")
#     elif opcion == "4":
#         print("las bebidas disponibles son:")
#         for bebida in bebidas:
#             print(f"- {bebida}")
#         eleccion = input("¿Qué bebida desea comprar? ")
#         if eleccion in bebidas:
#             try:
#                 print(f"Ha comprado una {eleccion}. ¡Gracias por su compra!")
#                 mensaje = "Ha comprado una  " + eleccion + ". ¡Gracias por su compra!"
#                 data.write(mensaje + "\n")
#                 print("Compra registrada exitosamente.")
#             except Exception as e:
#                 print(e)
#                 print("Error al escribir en el archivo.")
#         else:
#             print("Lo siento, esa bebida no está disponible.")
#     elif opcion == "5":
#         print("Gracias por visitar el minimarket. ¡Hasta luego!")
#         data.close()
#         break
#     else:
#         print("Opción no válida. Por favor, intente de nuevo.")





def menu():
    print(mensaje_bienvenida)
    for opcion in opciones_menu:
        print(opcion)
    opcion = input("Ingrese el número de la opción deseada: ")
    return opcion

def tipo_producto(opcion):
    if opcion == "1":
        accion = seleccion_producto(frutas, "fruta")
        registrar_compra(accion, frutas)
        return accion
    elif opcion == "2":
        accion = seleccion_producto(verduras, "verdura")
        registrar_compra(accion, verduras)
        return accion
    elif opcion == "3":
        accion = seleccion_producto(snacks, "snack")
        registrar_compra(accion, snacks)
        return accion
    elif opcion == "4":
        accion = seleccion_producto(bebidas, "bebida")
        registrar_compra(accion, bebidas)
        return accion
    elif opcion == "5":
        accion = cerrar_archivo()
        return "salir", None
    else:
        return None
    
def seleccion_producto(lista_producto, tipo):
    print(f"las {tipo}s disponibles son:")
    for producto in lista_producto:
        print(f"- {producto}")
    seleccion = input(f"¿Qué {tipo} desea comprar? ")
    return seleccion

def registrar_compra(seleccion, tipo):
    if seleccion in tipo:
        try:
            print(f"Ha comprado una {seleccion}. ¡Gracias por su compra!")
            mensaje = f"Ha comprado una {seleccion}. ¡Gracias por su compra!"
            data.write(mensaje + "\n")
        except Exception as e:
            print(e)
            print("Error al escribir en el archivo.")
    else:
        print(f"Lo siento, esa {tipo} no está disponible.")

def cerrar_archivo():
    try:
        data.close()
        print("Archivo cerrado correctamente.")
    except Exception as e:
        print(e)
        print("Error al cerrar el archivo.")


# # # V2
while True:
    opcion = menu()
    seleccion = tipo_producto(opcion)
    if seleccion == ("salir", None):
        break