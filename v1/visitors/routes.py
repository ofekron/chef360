from flask_restplus import Resource
from ..api import api



ns_res = api.namespace('visitors', description='Visitors operations')


@ns_res.route('/')
class VisitorsAPI(Resource):
    def get(self):
        """
        returns all visitors
        """
        return ["visitor1","visitor2"]

@ns_res.route('/<string:visitor_id>')
class VisitorAPI(Resource):
    def get(self,visitor_id):
        """
        returns a visitor
        """
    def put(self, visitor_id):
        """
        Edit visitor
        """