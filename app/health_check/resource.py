from flask import jsonify
import flask_restful as restful

class HealthCheckResource(restful.Resource):

    def get(self):
        return jsonify({"message" : "I'm okay"})