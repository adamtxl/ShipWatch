# app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

# New route for API
@app.route('/api/cruise_prices', methods=['GET'])
def get_cruise_prices():
    sample_data = {
        "cruises": [
            {"destination": "Bahamas", "price": "$500"},
            {"destination": "Alaska", "price": "$1200"},
            {"destination": "Mediterranean", "price": "$900"}
        ]
    }
    return jsonify(sample_data)

if __name__ == '__main__':
    app.run(debug=True)