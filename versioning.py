from flask import Blueprint
from flask_restplus import Api
def version(name):
    blueprint = Blueprint(name, __name__, url_prefix=f'/api/{name}')
    api = Api(blueprint, doc="/doc/", version=name)
    return blueprint,api