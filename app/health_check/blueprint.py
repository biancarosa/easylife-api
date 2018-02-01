from flask import Blueprint
from flask_restful import Api

from .resource import HealthCheckResource

def get_blueprint():
    blueprint = Blueprint('Health Check', __name__)
    api = Api(blueprint)
    api.add_resource(HealthCheckResource, '/health-check')
    return blueprint