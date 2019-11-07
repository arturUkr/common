from flask import request
from flask_restful import Resource, reqparse, fields, marshal_with
import json
from flask_rest_api.rooms.room_obj import Rooms


with open('rooms/rooms_data.json', 'r') as f:
    data_rooms_json = json.load(f)

DATA_ROOMS = []
for room in data_rooms_json:
    DATA_ROOMS.append(
        Rooms(number=room.get('number'),
              level=room.get('level'),
              status=room.get('status'),
              price=room.get('price'))
    )

room_structure = {
    "number": fields.Integer,
    "level": fields.Integer,
    "status": fields.String,
    "price": fields.Float

}

room_parser = reqparse.RequestParser(bundle_errors=True)
room_parser.add_argument('status', type=str)   # available, closed


class RoomList(Resource):
    @marshal_with(room_structure)
    def get(self):
        args = room_parser.parse_args(strict=True)
        if args['status']:
            return [room for room in DATA_ROOMS if room.status == args['status']]
        else:
            return DATA_ROOMS

    def post(self):
        result = request.json
        all_room_number = [room.number for room in DATA_ROOMS]
        if result['number'] not in all_room_number:
            DATA_ROOMS.append(
                Rooms(number=result.get('number'),
                      level=result.get('level'),
                      status=result.get('status'),
                      price=result.get('price'))
            )
            return 'post'
        else:
            return 'This number is blocked'

    def patch(self):
        result = request.json
        for room in DATA_ROOMS:
            if room.number == result['number']:
                room.level = result['level'] if result.get('level') else room.level
                room.status = result['status'] if result.get('status') else room.status
                room.price = result['price'] if result.get('price') else room.price
        return 'patch'


class RoomNumber(Resource):
    @marshal_with(room_structure)
    def get(self, room_number):
        return [room for room in DATA_ROOMS if room.number == room_number]

    def delete(self, room_number):
        DATA_ROOMS[:] = [room for room in DATA_ROOMS if room.number != room_number]
        return 'delete'
