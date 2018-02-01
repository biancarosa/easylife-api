from flask import jsonify
import flask_restful as restful

from .model import Income

class IncomesResource(restful.Resource):

    def post(self):
        req = self.request.json()
        income = Income()
        income.amount = req.get('amount')
        income.reference_month = req.get('reference_month')
        income.save()
        return jsonify({"data" : income.to_json()}), 201

    def get(self):
        incomes = Income.objects()
        data = []
        for income in incomes:
            data.append(income.to_json())
        return jsonify({"data" : incomes, "success" : True}), 201
