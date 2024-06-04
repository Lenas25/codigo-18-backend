import bcrypt
# libreria para encriptar la contraseña a partir de un string

# funcion para encriptar la contraseña con la libreria bcrypt
def encrypt_password(password):
    """
    generar un salt un numero aleatorio que se genera y 
    es concatenado a la contraseña, este se usa por seguridad y para 
    evitar ataques de fuerza bruta
    """
    salt = bcrypt.gensalt()
    # primero el password se convierte a bytes y luego se encripta con el salt y el hashpw cifra la contraseña, retorna un texto encriptado en bytes
    return bcrypt.hashpw(password.encode('utf-8'), salt)