from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

DATA_PATH = os.path.join(os.path.dirname(__file__), 'data', 'mock_data.json')

def load_data():
    with open(DATA_PATH, 'r') as f:
        return json.load(f)

@app.route('/api/order/<order_id>', methods=['GET'])
def get_order_status(order_id):
    """
    Handles "Where is my order?"
    Returns order details or 404.
    """
    data = load_data()
    for order in data.get('orders', []):
        if order['order_id'] == order_id:
            return jsonify({
                "success": True,
                "order_id": order['order_id'],
                "status": order['status'],
                "carrier": order['carrier'],
                "tracking_url": order['tracking_url'],
                "estimated_delivery": order['estimated_delivery']
            })
    
    return jsonify({"success": False, "error": "Order ID not found"}), 404

@app.route('/api/returns', methods=['POST'])
def get_return_policy():
    """
    Handles "How do I return this?"
    Expects JSON: {"category": "Electronics"}
    """
    data = load_data()
    payload = request.get_json()
    if not payload:
        return jsonify({"success": False, "error": "Missing JSON body"}), 400
    
    category = payload.get('category', '').capitalize()
    
    for policy in data.get('returns', []):
        if policy['category'].lower() == category.lower():
            return jsonify({
                "success": True,
                "category": category,
                "window_days": policy['window_days'],
                "condition": policy['condition'],
                "refund_method": policy['refund_method']
            })
    
    return jsonify({
        "success": False,
        "error": f"Policy not found for category: {category}",
        "suggestion": "Please contact support for unknown categories."
    }), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
