# SIN FLASK NI ORMS
from MySQLdb import _mysql

# con una base de datos ya creada
conexion = _mysql.connect(host='localhost', user='root', password='root', database='introduccion')

# para hacer peticiones
conexion.query('SELECT * FROM usuarios')

# guardar el resultado en una variable
resultado = conexion.store_result()
#capturar las respuestas, fetch_row() trae la primera fila, lo imprime como tupla
print(resultado.fetch_row())