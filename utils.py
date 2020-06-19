from functools import wraps

from flask import Blueprint, request
from flask_restplus import Api, Resource

api_token_header='X-API-KEY'
auth={
        'apikey' : {
            'type' : 'apiKey',
            'in' : 'header',
            'name' : api_token_header
        }
}
def version(name):
    blueprint = Blueprint(name, __name__, url_prefix=f'/api/{name}')
    api = Api(blueprint, doc="/docs/", version=name,authorizations=auth, security='apikey')
    return blueprint,api

def token_required(f):
    @wraps(f)
    def _token_validate(*args, **kwargs):
        if api_token_header in request.headers:
            if request.headers[api_token_header]=="token1":
                return f(*args, **kwargs)
        return {'error' : 'unauthurized access'},401
    return _token_validate


class SecuredResource(Resource):
    def __init__(self, api=None, *args, **kwargs):
        Resource.__init__(self, api, *args, **kwargs)
        self.method_decorators = [token_required]
