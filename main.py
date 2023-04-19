from flask import Flask, request, jsonify

app = Flask(__name__)

data = {
    'A': {'price': 10.28, 'part': 'LED Screen'},
    'B': {'price': 24.07, 'part': 'OLED Screen'},
    'C': {'price': 33.30, 'part': 'AMOLED Screen'},
    'D': {'price': 25.94, 'part': 'Wide-Angle Camera'},
    'E': {'price': 32.39, 'part': 'Ultra-Wide-Angle Camera'},
    'F': {'price': 18.77, 'part': 'USB-C Port'},
    'G': {'price': 15.13, 'part': 'Micro-USB Port'},
    'H': {'price': 20.00, 'part': 'Lightning Port'},
    'I': {'price': 42.31, 'part': 'Android OS'},
    'J': {'price': 45.00, 'part': 'iOS OS'},
    'K': {'price': 45.00, 'part': 'Metallic Body'},
    'L': {'price': 30.00, 'part': 'Plastic Body'}
}


@app.route('/orders', methods=['POST'])
def create_order():
    components = request.json['components']
    total = round(sum(data[c]['price'] for c in components), 2)
    parts = [data[c]['part'] for c in components]
    order_id = "some-id"

    response = {
        "order_id": order_id,
        "total": total,
        "parts": parts
    }

    return jsonify(response), 201


if __name__ == '__main__':
    app.run()

