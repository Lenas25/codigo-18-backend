from flask import Flask, jsonify, request
# Flask -> clase que permite crear un servidor web
# jsonify -> convierte un diccionario en un json
# request -> permite obtener la informacion que envia el usuario
from utils import encrypt_password
# importa la funcion de encriptar la contraseña
from config import Config #importa la clase Config
from extensions import db, migrate #importa las instancias de db y migrate
from entities.users_model import User #importa la clase User
from flask_cors import CORS

app = Flask(__name__)  # __name__ == '__main__'
app.config.from_object(Config) #lee la clase y las variables de config las cargara en flask (buena practica)

CORS(app)

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
# ! CREATE
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
        return jsonify({
            'error': str(e),
            'linea': e.__traceback__.tb_lineno
        }),400

# ! UPDATE
@app.route('/api/v1/user/<int:id>', methods=['PUT'])
def update_user(id):
    try:
        user = User.query.get(id) #obtiene el usuario por el id
        if user is None:
            return jsonify({'error': 'User not found'})

        # verificar que datos son los que se estan enviando
        user_data = request.get_json() #obtiene la informacion que envia el usuario
        if 'full_name' in user_data:
            user.full_name = user_data['full_name']
        
        if 'email' in user_data:
            user.email = user_data['email']
        
        if 'password' in user_data:
            user.password = encrypt_password(user_data['password']).decode('utf-8')
        
        if 'phoneNumber' in user_data:
            user.phoneNumber = user_data['phoneNumber']
        
        if 'gender' in user_data:
            user.gender = user_data['gender']
        
        db.session.commit() #guarda los cambios en la db
        return jsonify({'message': 'User updated'})

    except Exception as e:
        return {'error': str(e)},400


# ! DELETE
@app.route('/api/v1/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        user = User.query.get(id) #obtiene el usuario por el id
        if user is None:
            return jsonify({'error': 'User not found'})
        
        db.session.delete(user) #elimina el usuario
        db.session.commit() #guarda los cambios en la db
        return jsonify({'message': 'User deleted'})
    except Exception as e:
        return jsonify({'error': str(e)}),400


# depende del entorno el __name__ puede cambiar
if __name__ == '__main__':
    # el app_context() permite que se ejecute el codigo dentro de la funcion
    with app.app_context():
        db.create_all() #el create_all() crea las tablas en la db

    # permite que se reinicie el servidor automaticamente cada vez que se haga un cambio en el codigo
    app.run(debug=True)
