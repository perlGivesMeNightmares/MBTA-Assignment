from flask_restful import Resource
from src.core_commands.get_subway_routes import (
    get_subway_routes,
    GetRoutesUnexpectedResponseJsonFormatError,
)
from src.service_facade.mbta_request import TooManyRequestsException


class GetMBTASubwayRoutes(Resource):
    def get(self):
        try:
            return {"routes": get_subway_routes()}
        except GetRoutesUnexpectedResponseJsonFormatError:
            # TODO: look up how flask returns error
            return {"status": 500}
        except TooManyRequestsException:
            # Same as above, probably better to just retry with backoff
            return {"status": 500}
