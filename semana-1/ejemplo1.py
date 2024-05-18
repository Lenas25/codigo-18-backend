class Persona:
    """
    Existe una funcion que se ejecuta cuando instanciamos a nuestra clase, a esa funcion se le dice constructor, podemos tener mas de 1 y la forma de definirlo es con __init__.
    """

    """
    Cuando estamos dentro de una clase el primer parameto de todas las funciones sera self, luego del self podemos colocar mas parametros
    """

    def __init__(self, nombre, apellido, edad, altura, direccion, peso):
        self.__nombre = nombre;
        self.__apellido = apellido;
        self.edad = edad;
        self.altura = altura;
        self.__direccion = direccion;
        self.peso = peso;

    def saludar(self):
        return f"Hola {self.__nombre} {self.__apellido}, tu edad es {self.edad}"
    
    # reto: crear la funcion que retorne la direccion de la persona
    def direccion(self):
        return f"Tu direccion es: {self.__direccion}"

"""
Para instancia una clase, debemos simplemente llamarla por su nombre y guardarla en una variable
"""
persona1 = Persona("Pepe", "Perez", 18, 1.54, "Av.Sol 345",54);
# como es privado no se puede editar el valor
persona1.__nombre = "Elena"
# aqui si se puede editar porque es publico el atributo
# persona1.edad = 20
print(persona1.saludar());
print(persona1.direccion())