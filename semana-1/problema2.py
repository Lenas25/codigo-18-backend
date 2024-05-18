#  escribir un programa el cual me diga si un numero es par o impar


def par_impar(numero):

    mensaje = "El numero es impar"

    try:
        # es una manera de usar if pero en una sola linea
        # print("El numero es par") if int(numero) % 2 == 0 else print("El numero es impar")
        # no es recomendable utilizar un else es mejor almacenar la informacion en una variable
        if int(numero) % 2 == 0:
            mensaje = "El numero es par"
        print(mensaje)
    except Exception as e:
        print("Error: ", e)
        print("Por favor ingrese un numero valido")


numero = input("Ingrese un numero: ")
par_impar(numero)
