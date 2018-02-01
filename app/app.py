from flask import Flask, jsonify, request
import mongoengine

from finances.incomes import blueprint as incomes_blueprint
from health_check import blueprint as health_check_blueprint


app = Flask(__name__)

app.config.from_pyfile('config.cfg')
mongoengine.connect(host=app.config['MONGODB_SETTINGS']['host'],
                    username=app.config['MONGODB_SETTINGS']['username'],
                    password=app.config['MONGODB_SETTINGS']['password'])

app.register_blueprint(incomes_blueprint.get_blueprint())
app.register_blueprint(health_check_blueprint.get_blueprint())
