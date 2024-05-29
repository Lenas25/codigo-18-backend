# SIN FLASK NI ORMS
from psycopg2 import connect;

conexion = connect("dbname=pruebas user=postgres password=root")

# el cursor es el que ingresa a la base de datos y realiza las peticiones
cursor = conexion.cursor()

cursor.execute('SELECT * FROM productos;')

# fetchmany(n) trae ciertos resultados, fetchAll() trae todas las filas, fetchone() trae la primera respuesta
respuesta = cursor.fetchmany(2);
# imprime en un array de tuplas
print(respuesta)