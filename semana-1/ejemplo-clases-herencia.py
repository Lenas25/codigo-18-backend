class Persona:
    def __init__(self, nombre, apellido, edad, altura, direccion, peso):
        self.__nombre = nombre;
        self.__apellido = apellido;
        self.edad = edad;
        self.altura = altura;
        self.direccion = direccion;
        self.peso = peso;

    def saludar(self):
        return f"Hola {self.__nombre} {self.__apellido}, tu edad es {self.edad}"
    
    # getter
    def getNombre(self):
        return self.__nombre;

    # setter
    def setNombre(self, nuevo):
        self.__nombre = nuevo


class Estudiante(Persona):
    def __init__(self, nombre, apellido, edad, carrera):
        # aqui si debe estar instanciado todos los atributos
        super().__init__(nombre, apellido, edad, altura=None, direccion=None, peso=None)
        self.carrera = carrera
    
    def imprimirNombre(self):
        return f"Hola {self.getNombre()}, estudio {self.carrera}"
    

estudiante1 = Estudiante("Elena", "Suarez", 19, "Ing.Software")
# estudiante1.setNombre("Ea") para moficiar usar un set
print(estudiante1.imprimirNombre())


def crear_usuario2(user):
    return user


# diccionario, es una mejor manera de manejar los parametros a tratar
print(
    crear_usuario2({
    "nombre": "Pepe",
    "apellido": "Perez",
    "username": "pepe3hs"
})
)