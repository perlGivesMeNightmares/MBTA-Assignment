"""
Implement a command to get all stops for a provided route id
"""
from src.service_facade.mbta_request import MBTARequest
import logging


class GetStopsUnexpectedResponseJsonFormatError(Exception):
    """Exception raised when the structure of the MBTA service response is not parsable by this command"""


def get_subway_stops(route_id: str):
    stop_display_name_attr = "name"
    stops = MBTARequest().fetch_stops_by_route_id(route_id, stop_display_name_attr)
    try:
        return [stop["attributes"][stop_display_name_attr] for stop in stops]
    except KeyError as ke:
        logging.getLogger(__name__).exception("add some error info here")
        raise GetStopsUnexpectedResponseJsonFormatError() from ke
