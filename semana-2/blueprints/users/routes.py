from flask import Blueprint, jsonify, request
from extensions import db
from entities.users_model import User
from utils import encrypt_password, check_password
from flask_jwt_extended import create_access_token, jwt_required

users_bp = Blueprint('users', __name__)

"""
Ruta para autenticas a los usuarios, el metodo es un POST cuando se autentica
"""
@users_bp.route('/api/v1/login', methods=['POST'])
def login():
    user_data = request.get_json();
    #paso 1 buscar al usuario por el email
    user = User.query.filter_by(email = user_data['email']).first()
    try:
        # paso 2 validar si el usuario existe
        if user is None:
            return jsonify({
                "message":"Email and/or password incorrect"
            }),400
        # paso 3 verificar si el password es el mismo de la bd
        # funcion que permite comparar 
        if check_password(user_data['password'].encode("utf-8"), user.password.encode("utf-8")):
            access_token = create_access_token(identity = user.id);
            return jsonify({
                "message":"User enter correct",
                "user": user.to_dict(),
                "access_token":access_token
            }),200

        return jsonify({
                "message":"Email and/or password incorrect"
            }),400
    except Exception as e:
        return jsonify({
            'error':str(e),
            'content':e.args
        }),400


# ! GET

@users_bp.route('/api/v1/users')
@jwt_required()
def get_all_users():
    try:
        # retorna la informacion en formato json de la base de datos, query.all() -> obtiene todos los registros de la tabla
        users = User.query.all()
        # recorre todos los registros de la tabla y los convierte en un diccionario y los guarda en la variable users
        return jsonify(
            {
                'users': [user.to_dict() for user in users]
            }
        )
    except Exception as e:
        return jsonify({
            'error': str(e),
            'linea': e.__traceback__.tb_lineno
        }), 400


# ! CREATE
@users_bp.route('/api/v1/user', methods=['POST'])
@jwt_required()
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
@users_bp.route('/api/v1/user/<int:id>', methods=['PUT'])
@jwt_required()
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
@users_bp.route('/api/v1/user/<int:id>', methods=['DELETE'])
@jwt_required()
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
    
# ! GET BY ID
@users_bp.route('/api/v1/user/<int:id>')
@jwt_required()
def get_user_by_id(id):
    try:
        user = User.query.get(id) #obtiene el usuario por el id
        if user is None:
            return jsonify({'error': 'User not found'})
        
        return jsonify(user.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}),400
