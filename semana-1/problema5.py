"""
Escribe una funcion max_de_tres que tome tres numeros como argumentos y regrese el mayor de ellos
"""

def max_de_tres(n1, n2, n3):
    # funcion max que regresa el mayor de los argumentos, si no se puede realizar con if 
    return max(n1, n2, n3)

# para ingresar los numeros en una sola linea
numeros = input("Escribe tres numeros separados por espacio: ")
# convertir los numeros en una lista, con un map se convierte una lista de strings en una lista de enteros
n1,n2,n3 = map(int, numeros.split())

print(max_de_tres(n1,n2,n3))