from flask_restful import Resource
from src.core_commands.get_subway_stops import (
    get_subway_stops,
    GetStopsUnexpectedResponseJsonFormatError,
)
from src.service_facade.mbta_request import TooManyRequestsException


class GetMBTASubwayStops(Resource):
    def get(self, route_id):
        try:
            return {"stops": get_subway_stops(route_id)}
        except GetStopsUnexpectedResponseJsonFormatError:
            # TODO: look up how flask returns error
            return {"status": 500}
        except TooManyRequestsException:
            # Same as above, probably better to just retry with backoff
            return {"status": 500}
