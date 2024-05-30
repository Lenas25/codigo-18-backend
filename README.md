# Flask API

## SLQAlchemy

En este proyecto estamos utilizando SQLAlchemy para la conexión con la base de datos, debido a que este es un ORM, no es necesario escribir SQL para realizar las consultas a la base de datos.

## Pasos para crear una tabla usando SQLAlchemy

- Crear una clase que herede de `db.Model`

```py
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
```

**Nota:** `db` es una variable que guarda la instancia de SQLAlchemy en el archvio `extensions.py`

- Importar el modelo creado, en este caso `User` en el archivo `app.py`

```py
from entities.user_model import User
```

**Por qué importar el modelo en `app.py`?** Porque es en este archivo va a cargar la migración en `app.py` y además nos va a permitir interactuar con la base de datos.

## Migrations con SLQAlchemy

Para crear una migración debemos ejecutar el siguiente comando:

```bash
flask db init
```

**Nota:** Este comando solo se ejecuta una vez, para inicializar las migraciones.

Para crear una migración debemos ejecutar el siguiente comando:

```bash
flask db migrate -m "mensaje"
```

**Nota:** El mensaje es opcional, pero es recomendable escribir un mensaje que describa los cambios realizados.

Para aplicar la migración debemos ejecutar el siguiente comando:

```bash
flask db upgrade
```

Este comando creará la tabla en la base de datos

## Exercises from SQLBolt
- Exercise 1 : Statements
  ```sql
  SELECT * FROM movies;
  SELECT title FROM movies;
  SELECT title, year FROM movies;
  ```
- Exercise 2 : Statements
  ```sql
  SELECT * FROM movies where year between 2000 and 2010;
  SELECT title, year FROM movies limit 5;
  ```
- Exercise 3 : Statements
  ```sql
  SELECT * FROM movies where director not like 'John Lasseter';
  SELECT * FROM movies where title like 'WALL-%';
  ```
- Exercise 4 : Statements
  ```sql
  SELECT city, longitude FROM north_american_cities WHERE longitude < -87.629798 ORDER BY longitude ASC;
  SELECT * FROM north_american_cities where country='United States' order by population desc limit 2 offset 2;
  ```
- Exercise 5 : Statements
  ```sql
  SELECT id, title, domestic_sales, international_sales FROM movies inner join boxoffice on boxoffice.movie_id=movies.id
  where international_sales>domestic_sales;
  SELECT DISTINCT building_name, role FROM buildings LEFT JOIN employees ON building_name = building;
  ```
