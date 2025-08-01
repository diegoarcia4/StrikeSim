from flask import Flask, jsonify, request
import json

app = Flask(__name__)

ladder_data = {
    "step": 4,
    "wager": 90.70,
    "payout": 204.07,
    "status": "Pending",
    "history": [
        {"step": 1, "wager": 15.00, "payout": 33.75, "status": "✅"},
        {"step": 2, "wager": 33.75, "payout": 75.94, "status": "✅"},
        {"step": 3, "wager": 40.31, "payout": 90.70, "status": "✅"}
    ]
}

@app.route('/api/ladder', methods=['GET'])
def get_ladder():
    return jsonify(ladder_data)

@app.route('/api/props', methods=['GET'])
def get_props():
    with open('props_today.json') as f:
        props = json.load(f)
    return jsonify(props)

@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({"status": "StrikeSim backend is running."})

if __name__ == '__main__':
    app.run(debug=True)
