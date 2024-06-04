from flask import Flask, jsonify
from sqlalchemy import Column, types
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.schema import ForeignKey
from datetime import datetime, timedelta
from flask_restful import Api, Resource, request
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import Schema, fields
from bcrypt import hashpw, gensalt, checkpw
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from crearCorreos import olvide_password
from cryptography.fernet import Fernet
from os import environ
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')
app.config['JWT_SECRET_KEY'] = environ.get('JWT_SECRET')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

#para jwt
jwt = JWTManager(app)

# para flask-restful
api = Api(app)

# para sqlalchemy
conexion = SQLAlchemy(app)

class Usuario(conexion.Model):
    __tablename__ = 'usuarios'

    id = Column(types.Integer, primary_key=True, autoincrement=True)
    nombre = Column(types.String(100), nullable=False)
    correo = Column(types.String(100), nullable=False, unique=True)
    password = Column(types.Text, nullable=False)
    createdAt = Column(types.DateTime, default=datetime.now(), name='created_at')

class Actividad(conexion.Model):
    __tablename__ = 'actividades'

    id = Column(types.Integer, primary_key=True, autoincrement=True)
    nombre = Column(types.Text, nullable=False)
    descripcion = Column(types.Text, nullable=False)
    habilitado = Column(types.Boolean, default=True)
    fecha = Column(types.DateTime)
    usuarioId = Column(ForeignKey(column='usuarios.id'), type_=types.Integer, nullable=False, name='usuario_id')

class ActividadDto(SQLAlchemyAutoSchema):
    class Meta:
        model = Actividad

class UsuarioDto(SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario

#dto manual
class LoginDto(Schema):
    correo = fields.Email(required=True, error_messages = {'required': 'El correo es requerido'})
    password = fields.Str(required=True, error_messages = {'required': 'La contraseña es requerida'}) 

class OlvidePasswordDto(Schema):
    correo = fields.Email(required=True, error_messages = {'required': 'El correo es requerido'})

class ReseteoPasswordDto(Schema):
    password = fields.Str(required=True, error_messages = {'required': 'La contraseña es requerida'})

class ActividadController(Resource):
    dto = ActividadDto()
    # proteger la ruta, indicando que se requiere un token en el header con la palabra Bearer para acceder
    @jwt_required()
    def post(self):
        data = request.get_json()
        # obtener el id del usuario actual mediante su token
        usuario_actual_id = get_jwt_identity()
        try:
            # validada y convertida a objeto
            data_serializada = self.dto.load(data)
            actividad = Actividad(**data_serializada, usuarioId=usuario_actual_id)
            print(actividad)
            conexion.session.add(actividad)
            conexion.session.commit()
            # de la entidad a un diccionario
            respuesta = self.dto.dump(actividad)
            return {
                'message': 'Actividad creada correctamente',
                'content': respuesta
            }, 201
        except Exception as e:
            return {
                'message': 'Error al crear la actividad',
                'error': e.args
            }, 400

    @jwt_required()
    def get(self):
        usuario_actual_id = get_jwt_identity()
        actividades = conexion.session.query(Actividad).filter_by(usuarioId=usuario_actual_id).all()
        respuesta = self.dto.dump(actividades, many=True)
        return {
            'message': 'Lista de actividades',
            'content': respuesta
        }, 200

class RegistroUsuarioController(Resource):
    dto = UsuarioDto()
    def post(self):
        data = request.get_json()
        try:
            data_serializada = self.dto.load(data)
            # actualizamos la contraseña de los datos validados, utilizando la función hashpw de bcrypt donde le pasamos la contraseña en bytes y el salt, y para volver a actualizar se debe convertir a string en utf-8
            data_serializada['password'] = hashpw(data_serializada['password'].encode('utf-8'), gensalt(10)).decode('utf-8')
            usuario = Usuario(**data_serializada)
            # de la entidad a un diccionario
            conexion.session.add(usuario)
            conexion.session.commit()
            return {
                'message': 'Usuario creado correctamente'
            }, 201
        except Exception as e:
            return {
                'message': 'Error al crear el usuario',
                'error': e.args
            }, 400

class LoginController(Resource):
    dto = LoginDto()
    def post(self):
        try:
            data = request.get_json()
            data_serializada = self.dto.load(data)
            #buscamos si el usuario existe
            usuario:Usuario | None = conexion.session.query(Usuario).filter_by(correo=data_serializada['correo']).first()
            if usuario is None:
                raise Exception('Usuario no existe')
            
            #comparamos la contraseña
            password_original = usuario.password.encode('utf-8')
            password_por_comparar = data_serializada['password'].encode('utf-8')
            resultado = checkpw(password_por_comparar, password_original)
            if not resultado:
                raise Exception('Usuario no existe')
            #generamos el token referente al id del usuario
            token = create_access_token(identity=usuario.id)    



            return {
                'message': 'Usuario logueado correctamente',
                'content': token
            }, 200
        except Exception as e:
            return {
                'message': 'Error al iniciar sesión',
                'error': e.args
            }, 400

class OlvidePasswordController(Resource):
    dto = OlvidePasswordDto()
    def post(self):
        try:
            data = self.dto.load(request.get_json())
            olvide_password(data['correo'])
            return {
                'message': 'Correo enviado correctamente'
            }, 200

        except Exception as e:
            return {
                'message': 'Error al validar los datos',
                'error': e.args
            }, 400

class ReseteoPasswordController(Resource):
    def post(self):
        try:
            dto = ReseteoPasswordDto()
            data = dto.load(request.get_json())
            query_params = request.args # para obtener las query params del url
            token = query_params['token']
            fernet = Fernet(environ.get('FERNET_KEY')) # la misma clave que se utilizó para encriptar
            correo = fernet.decrypt(token.encode('utf-8')).decode('utf-8')

            usuario = conexion.session.query(Usuario).filter_by(correo=correo).first()
            if usuario is None:
                raise Exception('Usuario no existe')
            # actualizamos la contraseña
            usuario.password = hashpw(data['password'].encode('utf-8'), gensalt(10)).decode('utf-8')
            conexion.session.commit()
            return {
                'message': 'Contraseña actualizada correctamente'
            }, 200
        except Exception as e:
            return {
                'message': 'Error al actualizar la contraseña',
                'error': e.args
            }, 400

api.add_resource(ActividadController, '/actividades')
api.add_resource(RegistroUsuarioController, '/signup')
api.add_resource(LoginController, '/login')
api.add_resource(OlvidePasswordController, '/olvide-password')
api.add_resource(ReseteoPasswordController, '/cambiar-password')

if __name__ == '__main__':
    # Crear la base de datos antes de iniciar la aplicación
    with app.app_context():
        conexion.create_all()

    app.run(debug=True)