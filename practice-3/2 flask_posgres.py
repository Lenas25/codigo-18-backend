from flask import Flask
from psycopg2 import connect

app = Flask(__name__)


def conexion_bd():
    conexion = connect(host='localhost', database='pruebas',
                       user='postgres', password='root')
    return conexion


@app.route('/', methods=['GET'])
def productos():
    # de esta manera es muy tedioso ya que se debe especificar manualmente los campos, para eso se usa el ORM tambien una herramienta muchos mas facil
    conexion = conexion_bd()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM productos;')
    respuesta = cursor.fetchall()
    resultado_mostrar = []
    # recorrer la respuesta
    for registro in respuesta:
        # para especificar los campos iterando manualmente
        producto = {
            'id': registro[0],
            'nombre': registro[1],
        }
        resultado_mostrar.append(producto)

    # ahora seria un array de diccionarios
    return {
        'content': resultado_mostrar,
    }


if __name__ == '__main__':
    app.run(debug=True)
