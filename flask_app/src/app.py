"""Start up the server"""
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from src.route_adapters.get_mbta_subway_routes import GetMBTASubwayRoutes
from src.route_adapters.get_mbta_subway_stops import GetMBTASubwayStops


app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(
    GetMBTASubwayRoutes,
    "/get_mbta_subway_routes",
    endpoint="get_mbta_subway_routes",
)
api.add_resource(
    GetMBTASubwayStops,
    "/get_mbta_subway_stops/<string:route_id>",
    endpoint="get_mbta_subway_stops",
)
