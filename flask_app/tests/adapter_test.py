from unittest.mock import MagicMock
import pytest
import src.route_adapters.get_mbta_subway_routes as get_mbta_subway_routes
import src.route_adapters.get_mbta_subway_stops as get_mbta_subway_stops

@pytest.fixture(autouse=True)
def context(mocker):
    mock_route_res = [{"id": "hurr", "name": "durr"}, {"id": "foo", "name": "bar"}]
    mocker.patch(f'{get_mbta_subway_routes.__name__}.get_subway_routes', return_value=mock_route_res)

    mock_stop_res = ["Stop A", "Stop B", "Stop C"]
    mocker.patch(f'{get_mbta_subway_stops.__name__}.get_subway_stops', return_value=mock_stop_res)


def test_get_routes_adapter():
    res = get_mbta_subway_routes.GetMBTASubwayRoutes().get()
    assert res