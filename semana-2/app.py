from flask import Flask
# Flask -> clase que permite crear un servidor web
from config import Config #importa la clase Config
from extensions import db, migrate, jwt  #importa las instancias de db, migrate y jwt
from flask_cors import CORS #CORS es un middleware que permite que se puedan hacer peticiones desde cualquier origen
#importa la variable que contiene las rutas
from blueprints.users.routes import users_bp
from blueprints.products.routes import products_bp 

app = Flask(__name__)  # __name__ == '__main__'
app.config.from_object(Config) #lee la clase y las variables de config las cargara en flask (buena practica)

CORS(app)

# estas dos clases necesitan como parametro la app de la instancia de flask para que sepan que estan trabajando con flask
db.init_app(app) # inicializa la db
migrate.init_app(app, db) # inicializa la migracion
jwt.init_app(app) # inicializa el jwt

app.register_blueprint(users_bp) #registra las rutas 
app.register_blueprint(products_bp) #registra las rutas

if __name__ == '__main__':
    # el app_context() permite que se ejecute el codigo dentro de la funcion
    with app.app_context():
        db.create_all() #el create_all() crea las tablas en la db

    # permite que se reinicie el servidor automaticamente cada vez que se haga un cambio en el codigo
    app.run(debug=True)
