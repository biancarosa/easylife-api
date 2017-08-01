from flask import Flask, jsonify, request

app = Flask(__name__)

app.config.from_pyfile('config.cfg')
mongoengine.connect(host=app.config['MONGODB_SETTINGS']['host'],
                    username=app.config['MONGODB_SETTINGS']['username'],
                    password=app.config['MONGODB_SETTINGS']['password'])

@app.route('/v1/health-check')
def health_check():
    return jsonify({"message" : "I'm okay"}), 200

# Finances module
@app.route('/v1/finances/incomes', method=['POST'])
def add_incomes():
    request.json()
