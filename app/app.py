from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/v1/health-check')
def health_check():
    return jsonify({"message" : "I'm okay"}), 200
