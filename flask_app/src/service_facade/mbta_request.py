from __future__ import annotations
import requests


class TooManyRequestsException(Exception):
    """Error raised when rate limited by the MBTA API. Can be mitigated with an API key or simply waited out."""


class MBTARequest:
    """
    Wraps functions that interface with the MBTA service. If an API key is required in the future, provide one in a constructor.

    If time permits, will create a custom session obj with configurable retry count and a long backoff to avoid getting rate limited.
    """

    API_VERSION = "v3"

    @property
    def base_url(self) -> str:
        return f"https://api-{self.API_VERSION}.mbta.com"

    def fetch_routes_by_transport_type(
        self, transport_types: set[int], filter_field: str | None
    ) -> dict:
        allowed_types = ",".join(
            [str(transport_type) for transport_type in transport_types]
        )
        route_type_filter = f"filter[type]={allowed_types}"
        route_url = f"{self.base_url}/routes?{route_type_filter}"
        if filter_field:
            route_url += f"&fields[route]={filter_field}"
        res = requests.get(route_url)
        self._check_for_bad_response(res)
        return res.json()["data"]

    def fetch_stops_by_route_id(self, route_id: str, filter_field: str | None) -> dict:
        route_filter = f"filter[route]={route_id}"
        route_url = f"{self.base_url}/stops?{route_filter}"
        if filter_field:
            route_url += f"&fields[stop]={filter_field}"
        res = requests.get(route_url)
        self._check_for_bad_response(res)
        return res.json()["data"]

    def _check_for_bad_response(self, res: requests.Response):
        if res.status_code >= 300:
            # Should probably raise different command errors for each status code, but this one's the most likely
            raise TooManyRequestsException()
        return
