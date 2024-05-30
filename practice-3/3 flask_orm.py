# CON POSTGRES

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, types
from sqlalchemy.sql.schema import ForeignKey
from flask_restful import Resource, Api
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS
from os import environ
from dotenv import load_dotenv

# cargar las variables de entorno con el archivo .env
load_dotenv()

# la primera url es la url de la pagina que quieres ver, la segunda url es la url del archivo json que contiene la documentacion de la api
SWAGGER_URL = '/api-docs'
API_URL = '/static/documentacion.json'

app = Flask(__name__)

CORS(app, resources=['*'], allow_headers=['*'], methods=['GET', 'POST', 'PUT', 'DELETE'])

configuracion_swagger = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config = {
    'app_name':'Documentacion de la API' # titulo de la pagina de la documentacion
})

#estamos agregando toda la configuracion del swagger a nuestro proyecto de flask
app.register_blueprint(configuracion_swagger)

# dialect://username:password@host:port/database
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URI')

api = Api(app)

# lo que hace es SQLALCHEMY busca de la variable app que es la instancia de Flask, tenga las configuraciones para el uso de la base de datos por medio de variables de entorno
conexion = SQLAlchemy(app)


class Trabajador(conexion.Model):
    __tablename__ = 'trabajadores'

    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
    nombre = Column(type_=types.String(length=100), nullable=False)
    habilitado = Column(type_=types.Boolean, default=True)


class Direccion(conexion.Model):

    __tablename__ = 'direcciones'

    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
    nombre = Column(type_=types.String(length=250), nullable=True)
    numero = Column(type_=types.Integer, nullable=True)
    # llave foranea, referenciado a la tabla trabajadores la columna id
    trabajadorId = Column(ForeignKey(column='trabajadores.id'),
                          type_=types.Integer, nullable=False, name='trabajador_id')


# deprecado en las ultimas versiones de flask
# @app.before_first_request
# def before_first_request():
#     conexion.create_all()
with app.app_context():
    conexion.create_all()


# ! trabajando con decoradores
@app.route('/trabajadores', methods=['GET', 'POST'])
def manejo_trabajadores():
    # conectarnos a la base de datos, para abrir una sesion
    if request.method == 'GET':
        # retorna una lista de instancias de la clase Trabajador y se iteran para obtener los datos, forzar a que resultado sea una lista de la clase Trabajador
        resultado: list[Trabajador] = conexion.session.query(Trabajador).all()
        trabajadores = []
        for trabajador in resultado:
            trabajadores.append({
                'id': trabajador.id,
                'nombre': trabajador.nombre,
                'habilitado': trabajador.habilitado
            })
        return {
            'content': trabajadores
        }
    elif request.method == 'POST':
        # obtener los datos del trabajador mandado por el cliente, nueva instancia de trabajador
        data = request.get_json()
        nuevoTrabajador = Trabajador(
            nombre=data['nombre'],
            habilitado=data['habilitado']
        )
        # agregar nuevo registro a la sesion solo de la instancia de trabajador o tabla
        conexion.session.add(nuevoTrabajador)
        # guardar los cambios en la base de datos
        conexion.session.commit()
        return {
            'message': 'Trabajador creado con exito'
        }


@app.route('/direcciones', methods=['POST'])
def gestion_direcciones():
    if request.method == 'POST':
        try:
            data = request.get_json()
            # como es tedioso indicar todos los cambios que se van a realizar, se puede hacer con destructuracion
            # nombre = '...', numero = 123 , trabajadorId = 1
            nuevaDireccion = Direccion(**data)
            conexion.session.add(nuevaDireccion)
            conexion.session.commit()
            return {
            'message': 'Direccion creada con exito'
            }
        except:
            # mala peticion entonces codigo de error 400
            return {
                'message': 'Error al crear la direccion'
            },400

# para obtener las direcciones de un trabajador en especial, se debe pasar el id del trabajador primero va el tipo de dato y luego el nombre de la variable
@app.route('/direccion/<int:trabajadorId>', methods=['GET'])
def devolver_direcciones(trabajadorId):
    # Select * from direcciones where trabajadorId = trabajadorId
    resultado: list[Direccion] = conexion.session.query(Direccion).filter_by(trabajadorId = trabajadorId).all()
    print(resultado)
    direcciones = []
    for dire in resultado:
        direcciones.append({
            'id': dire.id,
            'nombre': dire.nombre,
            'numero': dire.numero,
            'trabajadorId': dire.trabajadorId
        })
    return {
        'content':direcciones
    }

# ? Data Transfer Object -> un serializador, transferir la informacion a informacion legible y a un formato que pueda ser entendido por el cliente
class TrabajadorDTO(SQLAlchemyAutoSchema):
    # para pasar metadatos, modificando los atributos sin necesidad de modificar la clase
    class Meta:
        # sirve para indicar en que tabla o modelo se tiene que basar para hacer las validaciones
        model = Trabajador


# ! trabajando con recursos manera mas optima
class TrabajadorController(Resource):
    def get(self):
        trabajadores: list[Trabajador] = conexion.session.query(Trabajador).all()
        dto = TrabajadorDTO()
        # transforma la infromacion proveniente del orm a una informacion legible (diccionario)
        # NOTA: si yo le paso un listado de informacion entonces adicionalmente debo pasar many=True
        trabajadoresList = dto.dump(trabajadores, many = True);
        print(trabajadoresList)
        return {
            'message': trabajadoresList
        }
    
    def post(self):
        data = request.get_json()
        dto = TrabajadorDTO()
        # cargar la informacion y validar si es correcta, si no es correcta entonces emitira un error con las incorreciones, y si es correcta lo guarda en una tupla
        try:
            dataValidada = dto.load(data)
            nuevoTrabajador = Trabajador(**dataValidada);
            conexion.session.add(nuevoTrabajador)
            conexion.session.commit()
            return {
                'message':'Trabajador creado exitosamente'
            }
        except Exception as e:
            response = jsonify({
                'message': 'Error al crear el trabajador',
                'content': str(e)
            })
            response.status_code = 400
            return response

class TrabajadorUnitarioController(Resource):
    dto = TrabajadorDTO()
    def get(self, id):
        trabajador = conexion.session.query(Trabajador).filter_by(id = id).first()
        resultado=self.dto.dump(trabajador)
        return {
            'content': resultado
        }
    
    def put(self, id):
        trabajador = conexion.session.query(Trabajador).filter_by(id = id).first()
        if trabajador is None:
            return {
                'message':'Trabajador no encontrado'
            },404
        try:
            data = request.get_json()
            data_validada = self.dto.load(data)
            # modificar los datos del trabajador
            trabajador.nombre = data_validada.get('nombre')
            trabajador.habilitado = data_validada.get('habilitado', trabajador.habilitado)
            conexion.session.commit()
            return {
                'message':'Trabajador modificado exitosamente'
            }
        except:
            return {
                'message':'Error en la peticion'
            },400

    def delete(self, id):
        trabajador = conexion.session.query(Trabajador).filter_by(id = id).first()
        direciones = conexion.session.query(Direccion).filter_by(trabajadorId = id).all()
        if trabajador is None:
            return {
                'message':'Trabajador no encontrado'
            },404
        
        if len(direciones) != 0:
            return {
                'message':'Trabajador no puede ser eliminado, tiene direcciones asociadas, elimine primero las direcciones'
            },400
        
        conexion.session.delete(trabajador)
        conexion.session.commit()
        return {
            'message':'Trabajador eliminado exitosamente'
        }


# se agrega la clase TrabajadorController a la ruta /api/trabajadores
api.add_resource(TrabajadorController,'/api/trabajadores')
api.add_resource(TrabajadorUnitarioController,'/api/trabajador/<int:id>')


if __name__ == '__main__':
    app.run(debug=True)
