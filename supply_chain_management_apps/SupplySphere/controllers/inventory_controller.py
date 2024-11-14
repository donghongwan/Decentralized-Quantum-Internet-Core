from flask import Blueprint, request, jsonify
from models import Inventory, db

bp = Blueprint('inventory', __name__)

@bp.route('/inventory', methods=['POST'])
def add_inventory():
    data = request.json
    new_inventory = Inventory(product_id=data['product_id'], quantity=data['quantity'], location=data['location'])
    db.session.add(new_inventory)
    db.session.commit()
    return jsonify({"id": new_inventory.id}), 201
