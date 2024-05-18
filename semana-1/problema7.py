"""

Escribe una function contar_palabras que reciba una cadena y deuvelva el numero de palabras que contiene

hola como estas -> 3

"""

def contar_palabras(cadena):
    return len(cadena.split())

cadena = input("Escribe una cadena: ")
print(contar_palabras(cadena))