"""
Super barebones test to verify the commands logic isn't broken.
TODO on testing error cases.

If time permitted I would build a set of potential API responses and then patch in the mocks. Hitting third party APIs in this kind of test is not greate...
"""
from src.core_commands.get_subway_routes import get_subway_routes
from src.core_commands.get_subway_stops import get_subway_stops


def test_get_subway_routes_happy_path():
    res = get_subway_routes()
    assert {
        "id": "Red",
        "name": "Red Line",
    } in res  # possibly flaky if red line goes down
    assert len(res) > 5


def test_get_subway_stops_happy_path():
    res = get_subway_stops("Green-B")
    assert "Hynes Convention Center" in res
    assert len(res) > 20
