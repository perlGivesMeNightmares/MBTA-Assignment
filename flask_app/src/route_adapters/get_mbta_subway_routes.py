from flask import make_response
from flask_restful import Resource, abort
from src.core_commands.get_subway_routes import get_subway_routes
from src.service_facade.mbta_request import TooManyRequestsError, BadClientRequestError


class GetMBTASubwayRoutes(Resource):
    def get(self):
        try:
            return {"routes": get_subway_routes()}
        except (TooManyRequestsError, BadClientRequestError):
            # Should provide some custom messages here
            abort(make_response({"message": "Bad request"}, 400))
        except Exception:
            # TODO: Check for the various types of custom errors and provide detail in this res
            abort(make_response({"message": "Add some error info"}, 500))
