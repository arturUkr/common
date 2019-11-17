from flask import Blueprint
from flask_restful import Api

from rooms.resource import RoomList

room_bp = Blueprint('rooms', __name__)
api = Api(room_bp)


api.add_resource(RoomList, '/rooms', '/rooms/<int:room_number>')
