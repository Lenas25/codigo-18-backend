from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager


# instancia de la clase SQLAlquemny para realizar operaciones con la db
db = SQLAlchemy()
# instancia de la clase Migrate para realizar migraciones en la db, la migracion sirve para que se actualice la db con los cambios que se hagan en los modelos
migrate = Migrate()
# instancia de la clase JWTManager para manejar la autenticacion con JWT
jwt = JWTManager()