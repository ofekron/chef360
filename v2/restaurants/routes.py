from utils import SecuredResource
from ..api import api

ns_res = api.namespace('restaurants', description='Restaurant operations')

@ns_res.route('/')
class RestaurantsAPI(SecuredResource):
    def get(self):
        """
        returns all restaurants
        """
        return ["Restaurant1","Restaurant2"]


@ns_res.route('/<string:restaurant_id>')
class RestaurantAPI(SecuredResource):
    def get(self,restaurant_id):
        """
        returns a restaurant by id
        """

    def put(self, restaurant_id):
        """
        Edit restaurant
        """