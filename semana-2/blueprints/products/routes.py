from flask import Blueprint, jsonify, request
# jsonify -> convierte un diccionario en un json
# request -> permite obtener la informacion que envia el usuario
# Blueprint -> clase que permite crear rutas
from extensions import db
from entities.product_model import Product

products_bp = Blueprint('products', __name__)

# ! GET
@products_bp.route('/api/v1/products')
def get_all_products():
    try:
        products = Product.query.all()
        return jsonify(
            {
                'products': [pro.to_dict() for pro in products]
            }
        )
    except Exception as e:
        return jsonify({
            'error': str(e),
            'linea': e.__traceback__.tb_lineno
        }), 400


# ! CREATE
@products_bp.route('/api/v1/product', methods=['POST'])
def create_product():
    try:
        product_data = request.get_json()
        new_product  = Product(
            name=product_data['name'],
            description=product_data['description'],
            price=product_data['price'],
            stock=product_data['stock']
        )

        db.session.add(new_product) #agrega el nuevo usuario a la db
        db.session.commit() #guarda los cambios en la db

        return jsonify({'new_product': product_data})
    except Exception as e:
        return jsonify({
            'error': str(e),
            'linea': e.__traceback__.tb_lineno
        }),400

# ! UPDATE
@products_bp.route('/api/v1/product/<int:id>', methods=['PUT'])
def update_product(id):
    try:
        product = Product.query.get(id) #obtiene el usuario por el id
        if product is None:
            return jsonify({'error': 'Product not found'})

        product_data = request.get_json() #obtiene la informacion que envia el usuario
        if 'name' in product_data:
            product.name = product_data['name']
        
        if 'description' in product_data:
            product.description = product_data['description']
        
        if 'price' in product_data:
            product.price = product_data['price']
        
        if 'stock' in product_data:
            product.stock = product_data['stock']
        
        db.session.commit() #guarda los cambios en la db
        return jsonify({'message': 'Product updated'})

    except Exception as e:
        return {'error': str(e)},400


# ! DELETE
@products_bp.route('/api/v1/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    try:
        product = Product.query.get(id) 
        if product is None:
            return jsonify({'error': 'Product not found'})
        
        db.session.delete(product) 
        db.session.commit() 
        return jsonify({'message': 'Product deleted'})
    except Exception as e:
        return jsonify({'error': str(e)}),400
    
# ! GET BY ID
@products_bp.route('/api/v1/product/<int:id>')
def get_product_by_id(id):
    try:
        product = Product.query.get(id) #obtiene el usuario por el id
        if product is None:
            return jsonify({'error': 'Product not found'})
        
        return jsonify(product.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}),400