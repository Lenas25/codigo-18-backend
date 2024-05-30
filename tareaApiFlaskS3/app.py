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

load_dotenv()

app = Flask(__name__)

CORS(app)

# es de la clase API, se encarga de manejar las rutas de la api de flask_restful
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URI')
db = SQLAlchemy(app)

# ! para documentacion
SWAGGER_URL = '/api-docs'
API_URL = '/static/documentacion.json'

configuracion_swagger = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config = {
    'app_name':'Documentacion de la API Flask de Empresa' # titulo de la pagina de la documentacion
})

#estamos agregando toda la configuracion del swagger a nuestro proyecto de flask
app.register_blueprint(configuracion_swagger)


# tabla Areas
class Areas(db.Model):
    __tablename__ = 'areas'

    id = Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = Column(db.String(100), nullable=False)
    piso = Column(db.Integer, nullable=False)

# tabla Empleados
class Empleados(db.Model):
    __tablename__ = 'empleados'

    id = Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = Column(db.String(100), nullable=False)
    apellido = Column(db.String(100), nullable=False)
    email = Column(db.String(100), unique=True, nullable=False)
    # llave foranea, referenciado a la tabla areas la columna id
    areaId = Column(ForeignKey('areas.id'), type_=types.Integer,
                    nullable=False, name='area_id')

# ? Data Transfer Object -> un serializador, transferir la informacion a informacion legible y a un formato que pueda ser entendido por el cliente


class AreasDTO(SQLAlchemyAutoSchema):
    # para pasar metadatos, modificando los atributos sin necesidad de modificar la clase
    class Meta:
        # sirve para indicar en que tabla o modelo se tiene que basar para hacer las validaciones
        model = Areas
        # load_instance = True


class EmpleadosDTO(SQLAlchemyAutoSchema):
    # para pasar metadatos, modificando los atributos sin necesidad de modificar la clase
    class Meta:
        # sirve para indicar en que tabla o modelo se tiene que basar para hacer las validaciones
        model = Empleados
        # load_instance = True
        include_fk = True  # Incluye claves foráneas en la serialización si hay alguna

# ! trabajando con recursos


class AreasController(Resource):
    dto = AreasDTO()

    def get(self):
        areas: list[Areas] = db.session.query(Areas).all()
        # transforma la infromacion proveniente del orm a una informacion legible (diccionario)
        # NOTA: si yo le paso un listado de informacion entonces adicionalmente debo pasar many=True
        areasList = self.dto.dump(areas, many=True);
        return {
            'areas': areasList
        }


class AreasPostController(Resource):
    dto = AreasDTO()

    def post(self):
        # deserializar la informacion
        data = request.get_json()
        try:
            data_validada = self.dto.load(data)
            new_area = Areas(**data_validada)
            db.session.add(new_area)
            db.session.commit()
            return jsonify({
                'message':'Area creada exitosamente'
            })
        except Exception as e:
            return {
                'message': 'Error al crear el area',
                'content': e.args
            }, 400

class AreaUnitariaController(Resource):
    dto = AreasDTO()
    def get(self, id):
        area = db.session.query(Areas).get(id)
        if area:
            resultado=self.dto.dump(area)
            return {
                'area': resultado
            }
        return {
            'message': 'El empleado no esta registrado'
        },400

class EmpleadoPostController(Resource):
    dto = EmpleadosDTO()
    def post(self):
        data = request.get_json()
        try:
            # deserializar la informacion -> convertir la informacion a un objeto de tipo Empleados, si la data no puede ser deserializada entonces lanzara un error y pasara al except
            data_validada = self.dto.load(data)
            new_empleado = Empleados(**data_validada)
            db.session.add(new_empleado)
            db.session.commit()
            return jsonify({
                'message':'Area creada exitosamente'
            })
        except Exception as e:
            return {
                'message': 'Error al crear el area',
                'content': e.args
            },400

class EmpleadosController(Resource):
    dto = EmpleadosDTO()
    def get(self, nombre = None):
        if nombre is None:
            empleados: list[Empleados] = db.session.query(Empleados).all()
            empleadosList = self.dto.dump(empleados, many = True)
            return {
                'empleados': empleadosList
            }
        
        empleadosFiltrado = db.session.query(Empleados).filter_by(nombre = nombre).all()
        if empleadosFiltrado:
            empleadosListFiltrado = self.dto.dump(empleadosFiltrado, many = True)
            return {
                'empleadosEncontrados': empleadosListFiltrado
            }
        
        return {
            'message': 'El empleado que desea buscar no esta registrado'
        },400

# se agrega la clase TrabajadorController a la ruta /api/trabajadores
api.add_resource(AreasController,'/areas')
api.add_resource(AreasPostController,'/area')
api.add_resource(AreaUnitariaController,'/area/<int:id>')
api.add_resource(EmpleadoPostController,'/empleado')
api.add_resource(EmpleadosController,'/empleados','/empleados/<string:nombre>') 


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)