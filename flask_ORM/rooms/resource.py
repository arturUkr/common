from flask_restful import Resource, marshal_with, reqparse
from flask import request
from models import RoomModel
from db import db
from rooms.structure import room_structure

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('status', type=str)  # available, closed


class RoomList(Resource):

    @marshal_with(room_structure)
    def get(self, room_number=None):
        status = parser.parse_args(strict=True).get('status')
        model_obj = RoomModel.query
        if room_number:
            return model_obj.get(room_number)
        elif status:
            return model_obj.filter(RoomModel.status == status).all()
        else:
            return model_obj.all()

    def post(self):
        data = request.json
        if isinstance(data, list):
            for room in data:
                new_room = RoomModel(**room)
                db.session.add(new_room)
            db.session.commit()
        else:
            new_room = RoomModel(**data)
            db.session.add(new_room)
            db.session.commit()
        return 'create new room'

    def delete(self, room_number=None):
        if room_number:
            room = RoomModel.query.get(room_number)
            if room:
                db.session.delete(room)
                db.session.commit()
                return 'delete room'
            else:
                return "there's no such room_number"
        else:
            return 'insert /rooms/<int:room_number>'

    def patch(self, room_number=None):
        if room_number:
            new_room = request.json
            old_room = RoomModel.query.get(room_number)

            if old_room:
                old_room.level = new_room.get('level')
                old_room.status = new_room.get('status')
                old_room.price = new_room.get('price')
                old_room.tenant_id = new_room.get('tenant_id')

                db.session.commit()
                return 'update room'
            else:
                return "there's no such room_number"
        else:
            return 'insert /rooms/<int:room_number>'

