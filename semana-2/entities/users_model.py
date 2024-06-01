from extensions import db
from datetime import datetime, timezone

# un modelo es una clase a nivel de codigo, se debe colocar como herencia para que sepa que es un modelo de la db


class User(db.Model):
    __tablename__ = 'users'

    # definir los tipos de datos que se van a guardar en la db
    id = db.Column(db.Integer, primary_key=True)
    # nullable=True -> puede ser nulo
    full_name = db.Column(db.String(150), nullable=True)
    email = db.Column(db.String(150), unique=True,  nullable=False)
    password = db.Column(db.String(150),  nullable=False)
    phoneNumber = db.Column(db.String(50), nullable=True)
    gender = db.Column(db.String(50), nullable=True)
    # debe crearse de forma automatica, utc hace referencia a la zona horaria
    created_at = db.Column(db.DateTime, default=datetime.now(
        timezone.utc), nullable=False)
    # parametro onupdate se usa para que se actualice la fecha cada vez que se modifique un registro
    updated_at = db.Column(db.DateTime, default=datetime.now(
        timezone.utc), onupdate=datetime.now(timezone.utc), nullable=False)

    # Para poder mostrar la informacion de la tabla en la respuesta de
    # mi api, debemos parsear la informacion a un diccionario
    # to_dict es un metodo para convertir la informacion de la tabla a un diccionario
    def to_dict(self):
        return {
            'id': self.id,
            'full_name': self.full_name,
            'email': self.email,
            'password': self.password,
            'phone_number': self.phoneNumber,
            'gender': self.gender,

        }
