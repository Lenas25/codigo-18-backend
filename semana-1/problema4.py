"""
Escribir un progrmaa donde el usuario escriba un texto y este lo invierta

Ejemplo
hola -> aloh

"""

def invertir_texto(texto):
    # return texto[::-1], este hace que se invierta el texto ya que los :: el paso de inicio no se especifica entonces es el final de la secuencia, el paso final por defecto es el inicio si no se especifica y -1 es el paso
    longitud = len(texto)
    cadena_invertida = ""
    # desde donde comienza, hasta donde termina y de cuanto en cuanto
    for num in range(longitud-1, -1, -1):
        # el end sirve para que no se haga un salto de linea
        cadena_invertida+= texto[num]
    return cadena_invertida



texto = input("Escribe un texto: ")
print(invertir_texto(texto))


# este if es para que el programa se ejecute solo si se ejecuta desde la terminal el name es el nombre del archivo 
# if __name__ == "__main__":
#     main()

