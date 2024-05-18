# escriba un programa que calcule el area de un circulo
import math

def area_circulo(radio):
    try:
        # math es un modulo de python que contiene funciones matematicas como pi
        area = math.pi * float(radio) ** 2
        # para poder redondear un numero se debe usar la funcion round(numero, cantidad de decimales)
        return f"El area del circulo es: {round(area, 2)}"
    except Exception as e:
        return f"Error: {e}\nPor favor ingrese un radio valido"


radio = input("Ingrese el radio del circulo: ")
print(area_circulo(radio))