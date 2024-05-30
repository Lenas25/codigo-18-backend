print("Hola Mundo");
nombre = "Lena";
print("Hola", nombre);

#combinado *args y **kwargs
def ilimitado(*args, **kwargs):
    print(args)
    print(kwargs)

ilimitado(1,"w", nombre="Lena", edad=25)