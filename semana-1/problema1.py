# escriba un programa que retorne la suma de 2 numeros

# para obtener el dato que se ingrese en consola
num1 = input("Ingrese el primer numero: ")
num2 = input("Ingrese el segundo numero: ")
print(type(num1), type(num2))

"""
Si se quiere convrtir un str a int se debe usar int() y a float float()
"""
try:
    suma = float(num1) + float(num2)
    print("La suma de los numeros es: ", suma)
except Exception as e:
    print("Error: ", e)
    print("Por favor ingrese numeros validos")
