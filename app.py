from flask import Flask, jsonify

app = Flask(__name__)

products = {
    "fridge": {"price": 1000, "quantity": 20, "status": "low"},
    "microwave": {"price": 500, "quantity": 10, "status": "medium"},
    "tv": {"price": 2000, "quantity": 5, "status": "high"}
}


@app.route('/')
def home():
    return 'API doorman - V1.0.0'

@app.route('/api/products/<nome>')
def get_product(nome):
    product = products.get(nome.lower())
    if product:
        return jsonify(product)
    else:
        return jsonify({"error": "PCould not find the product"}), 404
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)