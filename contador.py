import csv
import string
from collections import Counter

    
def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('Opción 1: Contador de palabras', accion1),
        '2': ('Opción 2: Contador de letras', accion2),
        '3': ('Opción 3: Contador de una letra', accion3),
        '4': ('Opción 4: Contador de una letra', accion4),
        '5': ('Salir', salir)
    }

    generar_menu(opciones, '5')


def accion1():
    print('Has elegido la opción 1')
    print("¿Cómo se llama el archivo?")
    nombre = input()
    text = open(nombre).read()
    words = text.split()
    num_words = len(words)
    print("el archivo contiene: " + str(num_words) + "palabras")


def accion2():
    print('Has elegido la opción 2')
    print("¿Cómo se llama el archivo?")
    nombre = input()
    text = open(nombre).read()
    contador = 0; 
    words = text.split()
    for word in words:
        contador += len(word)
    
    print("el archivo contiene: " + str(contador) + "caracteres")

def accion3():
    print('Has elegido la opción 3')
    print("¿Cómo se llama el archivo?")
    nombre = input()
    text = open(nombre).read()
    contador = 0; 
    words = text.split()
    print("escribe la letra: ")
    letra = input()
    for word in words:
        counter = Counter(word)
        contador += counter[letra]
    
    print("el archivo contiene: " + str(contador) + "caracteres " + letra)

def accion4():
    print('Has elegido la opción 3')
    print("¿Cómo se llama el archivo?")
    nombre = input()
    text = open(nombre).read()
    contador = 0; 
    words = text.split()
    print("escribe la palabra: ")
    palabra = input()
    for word in words:
        contador += word.count(palabra)
    
    print("el archivo contiene: " + str(contador) + "palabras " + palabra)


def salir():
    print('Saliendo')


if __name__ == '__main__':
    menu_principal()