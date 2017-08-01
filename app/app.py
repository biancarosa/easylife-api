from flask import Flask, jsonify, request
import mongoengine

from models.income import Income

app = Flask(__name__)

app.config.from_pyfile('config.cfg')
mongoengine.connect(host=app.config['MONGODB_SETTINGS']['host'],
                    username=app.config['MONGODB_SETTINGS']['username'],
                    password=app.config['MONGODB_SETTINGS']['password'])

@app.route('/v1/health-check')
def health_check():
    return jsonify({"message" : "I'm okay"}), 200

# Finances module
@app.route('/v1/finances/incomes', methods=['POST'])
def add_incomes():
    r = request.json()
    income = Income()
    income.amount = r.get('amount')
    income.reference_month = r.get('reference_month')
    income.save()
    return jsonify({"data" : income.to_json()}), 201

@app.route('/v1/finances/incomes', methods=['GET'])
def get_incomes():
    incomes = Income.objects()
    data = []
    for income in incomes:
        data.append(income.to_json())
    return jsonify({"data" : incomes, "success" : True}), 201
