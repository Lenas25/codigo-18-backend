"""

Escriban una funcion la cual reciba un numero entero y retorne la suma de sus valores

Ejemplo:
2536 -> 16

"""


def suma_de_digitos(numero):
    try:
        suma = 0
        for num in numero:
            suma += int(num)
        return suma
    except:
        return "Solo se permiten numeros enteros"


numero = input("Escribe un numero: ")
print(suma_de_digitos(numero))
