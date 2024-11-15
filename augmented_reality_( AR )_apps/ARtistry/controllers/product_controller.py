from flask import Blueprint, request, jsonify
from services.product_service import ProductService

bp = Blueprint('product', __name__)

@bp.route('/product', methods=['POST'])
def add_product():
    data = request.json
    product = ProductService.add_product(data['name'], data['description'], data['image'], data['price'], data['stock'])
    return jsonify({'id': product.id}), 201
