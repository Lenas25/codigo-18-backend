from flask import Flask, jsonify, request
# Flask -> clase que permite crear un servidor web
# jsonify -> convierte un diccionario en un json
# request -> permite obtener la informacion que envia el usuario
from utils import encrypt_password
# importa la funcion de encriptar la contraseña
from config import Config #importa la clase Config
from extensions import db, migrate #importa las instancias de db y migrate
from entities.users_model import User #importa la clase User
from entities.product_model import Product #importa la clase Product
from flask_cors import CORS
from blueprints.users.routes import users_bp #importa la variable users_bp que contiene las rutas de los usuarios
from blueprints.products.routes import products_bp #importa la variable products_bp que contiene las rutas de los productos

app = Flask(__name__)  # __name__ == '__main__'
app.config.from_object(Config) #lee la clase y las variables de config las cargara en flask (buena practica)

CORS(app)

# estas dos clases necesitan como parametro la app de la instancia de flask para que sepan que estan trabajando con flask
db.init_app(app) # inicializa la db

migrate.init_app(app, db) # inicializa la migracion

app.register_blueprint(users_bp) #registra las rutas 
app.register_blueprint(products_bp) #registra las rutas

if __name__ == '__main__':
    # el app_context() permite que se ejecute el codigo dentro de la funcion
    with app.app_context():
        db.create_all() #el create_all() crea las tablas en la db

    # permite que se reinicie el servidor automaticamente cada vez que se haga un cambio en el codigo
    app.run(debug=True)
