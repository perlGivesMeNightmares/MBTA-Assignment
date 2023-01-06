"""
Implement a command to get all available subway routes and format them by ID and Name
"""
from src.service_facade.mbta_request import MBTARequest
from src.core_commands.constants import TransportTypes


class GetRoutesUnexpectedResponseJsonFormatError(Exception):
    """Exception raised when the structure of the MBTA service response is not parsable by this command"""


def get_subway_routes():
    formatted_routes = []
    route_display_name_attr = "long_name"

    routes = MBTARequest().fetch_routes_by_transport_type(
        TransportTypes.SUBWAY(), route_display_name_attr
    )
    for route_data in routes:
        try:
            route_id_and_name = {
                "id": route_data["id"],
                "name": route_data["attributes"][route_display_name_attr],
            }
        except KeyError as ke:
            raise GetRoutesUnexpectedResponseJsonFormatError() from ke

        formatted_routes.append(route_id_and_name)

    return formatted_routes
