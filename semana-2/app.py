from flask import Flask, jsonify, request
# Flask -> clase que permite crear un servidor web
# jsonify -> convierte un diccionario en un json
# request -> permite obtener la informacion que envia el usuario
from utils import encrypt_password
# importa la funcion de encriptar la contraseña
from config import Config #importa la clase Config
from extensions import db, migrate #importa las instancias de db y migrate
from entities.users_model import User #importa la clase User

app = Flask(__name__)  # __name__ == '__main__'
app.config.from_object(Config) #lee la clase y las variables de config las cargara en flask (buena practica)

# estas dos clases necesitan como parametro la app de la instancia de flask para que sepan que estan trabajando con flask
# inicializa la db
db.init_app(app)
# inicializa la migracion
migrate.init_app(app, db)

@app.route('/')
def home():
    # retorna la informacion en formato json de la base de datos, query.all() -> obtiene todos los registros de la tabla
    users = User.query.all()
    # recorre todos los registros de la tabla y los convierte en un diccionario y los guarda en la variable users
    return jsonify(
        {
            'users': [ user.to_dict() for user in users]
        }
    )

"""
Ejemplo donde recibiremos la informacion del usuario pero desde POSTMAN, por defecto la url es get, si se entra a esta url desde el navegador dara error ya que no es un metodo GET sino POST
"""
@app.route('/api/v1/user', methods=['POST'])
def create_user():
    try:
        # request.get_json() -> obtiene la informacion que envia el usuario
        user_data = request.get_json()
        # decode es para convertir el texto en bytes a string
        user_data['password'] = encrypt_password(user_data['password']).decode('utf-8')
        # agrega la informacion del usuario a la varible new_user utilizando la clase User de la tabla pasandole los atributos para guardar en la db
        new_user  = User(
            full_name=f"{user_data['name']} {user_data['lastname']}",
            email=user_data['email'],
            password=user_data['password'],
            phoneNumber=user_data['phone_number'],
            gender = user_data['gender']
        )

        db.session.add(new_user) #agrega el nuevo usuario a la db
        db.session.commit() #guarda los cambios en la db

        return jsonify({'new_user': user_data})
    except Exception as e:
        return jsonify({'error': str(e)})


# depende del entorno el __name__ puede cambiar
if __name__ == '__main__':
    # el app_context() permite que se ejecute el codigo dentro de la funcion
    with app.app_context():
        db.create_all() #el create_all() crea las tablas en la db

    # permite que se reinicie el servidor automaticamente cada vez que se haga un cambio en el codigo
    app.run(debug=True)