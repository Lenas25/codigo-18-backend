from flask import Flask, request
from flask_cors import CORS

# inficar si nuetro archivo es el archivo principal ahi es donde se debe instanciar, si el arhivo es el principal su valor de __name__ es __main__
app = Flask(__name__)

CORS(app, resources=['*'], allow_headers=['*'], methods=['GET', 'POST', 'PUT', 'DELETE'])

# se trabajara con base de datos
productos = [
    {
        "nombre": "laptop",
        "precio": 8000
    },
    {
        "nombre": "mouse",
        "precio": 500.5
    },
    {
        "nombre": "teclado",
        "precio": 1000.80
    }
]

# un decorador es una forma en la cual podemos emplear la herencia sin necesda de modificar la clase padre, es una forma de extender la funcionalidad de una clase sin modificarla


@app.route('/')
def inicio():
    # modificar el comportamiento del metodo route de la clase Flask para evitar modificar el metodo en la misma clase
    return "Bienvenido a la pagina principal de la aplicacion, soy Lena y estas en la ruta /"

# endpoint, es la ruta que se le asigna a una peticion http donde estara el backend, parametro metodos para indicar que metodos http se pueden usar en la ruta


@app.route('/productos', methods=['GET', 'POST'])
def gestion_productos():
    if request.method == 'GET':
        return {
            'content': productos,
        }
    elif request.method == 'POST':
        # get_json() convierte la data entrante a un formato diccionario
        data = request.get_json()
        productos.append(data)
        return {
            'message': 'Producto agregado correctamente',
        }


@app.route('/productos/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def gestion_producto(id):
    if request.method == 'GET':
        limite = len(productos)
        if limite < id:
            return {
                'message': 'Producto no encontrado',
            }
        else:
            return {
                # arreglo comienza en posicion 0
                'content': productos[id],
            }
    elif request.method == "PUT":
        limite = len(productos)
        if limite < id:
            return {
                'message': 'Producto no encontrado',
            }
        else:
            data = request.get_json()
            productos[id] = data
            return {
                'message': 'Producto actualizado correctamente',
            }
    elif request.method == "DELETE":
        limite = len(productos)
        if limite < id:
            return {
                'message': 'Producto no encontrado',
            }
        else:
            productos.pop(id)
            return {
                'message': 'Producto eliminado correctamente',
            }



# llamamos al metodo run de la clase Flask
# cuando se ejectua nos dice que el servidor esta corriendo en la direccion http:// y la parte del debug esta off o sea que cada que hagamos un cambio tenemos que reiniciar el servidor
if __name__ == '__main__':
    # debug=True, nos permite reiniciar el servidor automaticamente cada que hagamos un cambio
    app.run(debug=True)

# luego aparece dos lineas cuando abrimos el navegador y escribimos la direccion http://, la primera parte de cada linea ser la direccon ip de quien hace la peticion, el metodo, la ruta y el codigo de respuesta
