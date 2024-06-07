import os
from datetime import timedelta
#funcion de python para importa al sistema operativo, donde se usa tecnica env para evitar que las credencias de la db esten publicas

#crear configuracion e indicar en que lugar esta establecida mi db
class Config:
    # string de conection
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/codigo_18_backend';
    SQLALCHEMY_TRACK_MODIFICATIONS = True; #sirve para que flask este atento a las modificaciones de los modelos
    JWT_SECRET_KEY="my_secret_key"
    JWT_ACCESS_TOKEN_EXPIRES=timedelta(days=30);