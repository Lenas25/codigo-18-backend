from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# instancia de la clase SQLAlquemny para realizar operaciones con la db
db = SQLAlchemy()
# instancia de la clase Migrate para realizar migraciones en la db, la migracion sirve para que se actualice la db con los cambios que se hagan en los modelos
migrate = Migrate()