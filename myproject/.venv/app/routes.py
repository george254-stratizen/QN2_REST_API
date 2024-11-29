from flask import Blueprint, request, jsonify

api_blueprint = Blueprint('api', __name__)

# In-memory "database" to store products
products = []

@api_blueprint.route('/products', methods=['POST'])
def add_product():
    """Add a new product."""
    data = request.get_json()

    # Validate input
    if not all(key in data for key in ['name', 'description', 'price']):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        price = float(data['price'])
    except ValueError:
        return jsonify({"error": "Price must be a number"}), 400

    # Create product
    product = {
        "name": data["name"],
        "description": data["description"],
        "price": price
    }
    products.append(product)
    return jsonify({"message": "Product created successfully", "product": product}), 201

@api_blueprint.route('/products', methods=['GET'])
def get_products():
    """Retrieve all products."""
    return jsonify({"products": products}), 200

@api_blueprint.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to MyProduct API! Use /products to interact."})

