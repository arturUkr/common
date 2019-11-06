from flask import request
from flask_restful import Resource, reqparse, fields, marshal_with
import json
from flask_rest_api.rooms.room_obj import Rooms


with open('rooms/rooms_data.json', 'r') as f:
    data_rooms_json = json.load(f)

data_rooms = []
for room in data_rooms_json:
    data_rooms.append(
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


class RoomsApi(Resource):

    @marshal_with(room_structure)
    def get(self, room_number=None):
        args = room_parser.parse_args(strict=True)
        if args['status']:
            print(args['status'])
            return [room for room in data_rooms if room.status == args['status']]
        if room_number:
            for room in data_rooms:
                if room.number == room_number:
                    return room
        else:
            return data_rooms

    def post(self):
        result = request.json
        all_room_number = [room.number for room in data_rooms]
        if result['number'] not in all_room_number:
            data_rooms.append(
                Rooms(number=result.get('number'),
                      level=result.get('level'),
                      status=result.get('status'),
                      price=result.get('price'))
            )
        return 'post'

    def patch(self):
        result = request.json
        for room in data_rooms:
            if room.number == result['number']:
                room.level = result['level'] if result['level'] else room.level
                room.status = result['status'] if result['status'] else room.status
                room.price = result['price'] if result['price'] else room.price
        return 'patch'

    def delete(self, room_number=None):
        room_id = room_number if room_number else request.json['number']
        for i in range(len(data_rooms)):
            if data_rooms[i].number == room_id:
                data_rooms.pop(i)
        return 'delete'
