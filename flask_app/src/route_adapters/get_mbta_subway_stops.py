from flask import make_response
from flask_restful import Resource, abort
from src.core_commands.get_subway_stops import (
    get_subway_stops,
    GetStopsUnexpectedResponseJsonFormatError,
)
from src.service_facade.mbta_request import TooManyRequestsError


class GetMBTASubwayStops(Resource):
    def get(self, route_id):
        try:
            return {"stops": get_subway_stops(route_id)}
        except GetStopsUnexpectedResponseJsonFormatError:
           abort(make_response({"message": "Bad request"}, 400))
        except TooManyRequestsError:
            # TODO: Check for the various types of custom errors and provide detail in this res
            abort(make_response({"message": "Add some error info"}, 500))
