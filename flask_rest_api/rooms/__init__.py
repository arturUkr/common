from flask import Blueprint
from flask_restful import Api
from flask_rest_api.rooms.resourse import RoomList, RoomNumber

api_rooms_bp = Blueprint('rooms', __name__)
api = Api(api_rooms_bp)


api.add_resource(RoomList, '/rooms')
api.add_resource(RoomNumber, '/rooms/<int:room_number>')
