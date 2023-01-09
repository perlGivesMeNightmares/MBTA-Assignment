from __future__ import annotations

import requests
import logging
from datetime import datetime
from requests.adapters import HTTPAdapter, Retry

logger = logging.getLogger(__name__)


class TooManyRequestsError(Exception):
    """Error raised when rate limited by the MBTA API. Can be mitigated with an API key or simply waited out."""
    available_at_dt: str

class MalformedApiResponseError(Exception):
    """Error raised when the service response lacks the expected `data` key"""


class BadClientRequestError(Exception):
    """Error raised when the service reports the request as invalid"""


class UnknownApiRequestError(Exception):
    """Error raised when the request returns a 500 error code"""


class MBTARequest:
    """
    Wraps functions that interface with the MBTA service. If an API key is required in the future, provide one in a constructor.

    If time permits, will create a custom session obj with configurable retry count and a long backoff to avoid getting rate limited.
    """

    API_VERSION = "v3"
    MAX_RETRIES = 3

    def __init__(self):
        self.session = requests.Session()
        # Note that this backoff is unusually high, it is intended as a stopgap until the rate limit is raised
        retries = Retry(total=self.MAX_RETRIES, backoff_factor=1.5, status_forcelist=[429, 500, 502, 503, 504])
        self.session.mount('http://', HTTPAdapter(max_retries=retries))

    @property
    def base_url(self) -> str:
        return f"https://api-{self.API_VERSION}.mbta.com"

    def fetch_routes_by_transport_type(self, transport_types: set[int], filter_field: str | None) -> dict:
        allowed_types = ",".join([str(transport_type) for transport_type in transport_types])
        route_type_filter = f"filter[type]={allowed_types}"
        route_url = f"{self.base_url}/routes?{route_type_filter}"
        if filter_field:
            route_url += f"&fields[route]={filter_field}"
        res = self.session.get(route_url)
        return self._unwrap_response(res)

    def fetch_stops_by_route_id(self, route_id: str, filter_field: str | None) -> dict:
        route_filter = f"filter[route]={route_id}"
        route_url = f"{self.base_url}/stops?{route_filter}"
        if filter_field:
            route_url += f"&fields[stop]={filter_field}"
        res = self.session.get(route_url)
        return self._unwrap_response(res)

    def _unwrap_response(self, res: requests.Response) -> dict:
        if res.status_code == 429:
            ratelimit_reset = res.headers['x-ratelimit-reset']
            logger.error(f"Currently capped by API request limit, available at {ratelimit_reset}")
            # TODO: strftime this to human readable
            raise TooManyRequestsError(available_at_dt=ratelimit_reset)

        if 300 <= res.status_code < 500:
            raise BadClientRequestError()

        if res.status_code >= 500:
            logger.error(f"Bad response - {res.text} of status {res.status_code}")
            raise UnknownApiRequestError()

        try:
            res_payload = res.json()
            return res_payload["data"]
        except (KeyError, ValueError, requests.JSONDecodeError) as e:
            logger.error(f"Unexpected result - {res.text}")
            raise MalformedApiResponseError() from e
