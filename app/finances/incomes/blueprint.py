from flask import Blueprint
from flask_restful import Api

from .resource import IncomesResource

def get_blueprint():
    blueprint = Blueprint('Incomes', __name__)
    api = Api(blueprint)
    api.add_resource(IncomesResource, '/v1/finances/incomes')
    return blueprint