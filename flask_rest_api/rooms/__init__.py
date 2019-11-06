from flask import Blueprint
from flask_restful import Api
from flask_rest_api.rooms.resourse import RoomsApi

api_rooms_bp = Blueprint('rooms', __name__)
api = Api(api_rooms_bp)


api.add_resource(RoomsApi, '/rooms', '/rooms/<int:room_number>')
