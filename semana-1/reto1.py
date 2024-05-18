import string

# 1. Ordenar una lista
# Escribe una función que reciba una lista de números y devuelva una nueva lista con los elementos ordenados de manera ascendente.


def ordenar_lista(lista):
    return sorted(lista)

# print(ordenar_lista([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))

# 2. Calcular el promedio de una lista
# Escribe una función que reciba una lista de números y devuelva el promedio de esos números.


def promedio_lista(lista):
    # sum() suma los elementos de una elemento iterable
    return sum(lista) / len(lista)

# print(promedio_lista([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))

# 3. Contar ocurrencias de un elemento
# Escribe una función que reciba una lista y un elemento, y devuelva el número de veces que ese elemento aparece en la lista.


def contar_ocurrencias(lista, elemento):
    # con count() se puede contar las ocurrencias de un elemento en una lista
    return lista.count(elemento)

# print(contar_ocurrencias([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], 5))

# 4. Suma de los primeros n números naturales
# Escribe una función que reciba un número entero positivo 'n' y devuelva la suma de los primeros 'n' números naturales.


def suma_n_naturales(n):
    # sum=0
    # for i in range(1, n):
    #     sum += i
    # return sum
    # range() retorna una secuencia de números, comenzando desde 1 hasta n+1
    return sum(range(1, n+1))

# print(suma_n_naturales(10))

# 5. Eliminar duplicados de una lista
# Escribe una función que reciba una lista y devuelva una nueva lista sin elementos duplicados.


def eliminar_duplicados(lista):
    # set() crea un conjunto con los elementos de la lista, los conjuntos no permiten elementos duplicados
    return list(set(lista))

# print(eliminar_duplicados([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))

# 6. Generar números primos
# Escribe una función que genere los primeros 'n' números primos.


def es_primo(num):
    if num < 2:
        return False
    # el rango va desde 2 a la raiz cuadrada del numero mas 1 que comenzaba desde el 2 y aumentaba
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generar_primos(n):
    primos = []
    num = 2
    # mientras que la longitud de la lista sea menor a los numeros establecidos
    while len(primos) < n:
        if es_primo(num):
            primos.append(num)
        num += 1
    return primos


print(generar_primos(10))


# 8. Contar letras en una cadena
# Escribe una función que reciba una cadena y devuelva un diccionario con el conteo de cada letra en la cadena.
def contar_letras(cadena):
    diccionario = {}
    for letra in cadena:
        if letra in diccionario:
            diccionario[letra] += 1
        else:
            diccionario[letra] = 1
    return diccionario

# print(contar_letras("hola mundo"))

# 9. Verificar si una cadena es un pangrama
# Escribe una función que reciba una cadena y devuelva True si es un pangrama (contiene todas las letras del alfabeto al menos una vez) y False en caso contrario.


def pangrama(cadena):
    # Convertir la cadena a minúsculas para que la verificación sea insensible a mayúsculas/minúsculas
    cadena = cadena.lower()

    # Verificar si todas las letras del alfabeto están presentes en la cadena
    return set(string.ascii_lowercase).issubset(cadena)

# print(pangrama("The quick brown fox jumps over the lazy dog"))


# 10. Calcular el factorial de un número
# Escribe una función que calcule el factorial de un número entero no negativo.
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

# print(factorial(5))
