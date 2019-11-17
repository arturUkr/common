from flask_restful import Resource, marshal_with, request, reqparse, marshal
from models import StaffModel, RoomModel
from staff.structure import staff_structure, staff_room_structure
from rooms.structure import room_structure
from db import db

staff_room_parser = reqparse.RequestParser()
staff_room_parser.add_argument('staff_id', type=int)
staff_room_parser.add_argument('room_id', type=int)


class StaffList(Resource):

    def get(self, passport_id=None):
        if passport_id:
            return marshal(StaffModel.query.get(passport_id), staff_structure)
        return marshal(StaffModel.query.all(), staff_structure)

    def post(self):
        data = request.json
        if isinstance(data, list):
            for staff in data:
                new_staff = StaffModel(**staff)
                db.session.add(new_staff)
            db.session.commit()
        else:
            new_staff = StaffModel(**data)
            db.session.add(new_staff)
            db.session.commit()

        return 'add new staff'

    def delete(self, passport_id=None):
        if passport_id:
            staff = StaffModel.query.get(passport_id)
            if staff:
                db.session.delete(staff)
                db.session.commit()
                return f"delete staff {staff.passport_id}"
            else:
                return f"there's no staff {staff.passport_id}"
        else:
            return 'insert /staff/<int:passport_id>'

    def patch(self, passport_id=None):
        if passport_id:
            new_staff = request.json
            old_staff = StaffModel.query.get(passport_id)

            if old_staff:
                old_staff.name = new_staff.get('name')
                old_staff.position = new_staff.get('position')
                old_staff.salary = new_staff.get('salary')

                db.session.commit()
                return f'update staff {passport_id}'
            else:
                return "there's no passport_id {passport_id}"
        else:
            return 'insert /staff/<int:passport_id>'


class RoomStaff(Resource):

    def get(self):
        args = staff_room_parser.parse_args()
        staff_id = args.get('staff_id')
        room_id = args.get('room_id')

        if staff_id:
            staff = StaffModel.query.get(staff_id)
            return marshal(staff.serve, room_structure)
        elif room_id:
            room = RoomModel.query.get(room_id)
            return marshal(room.roomms, staff_structure)

    def post(self):
        data = request.json
        if isinstance(data, list):
            for staff_room_data in data:
                staff_id = staff_room_data.get('staff_id')
                room_id = staff_room_data.get('room_id')
                staff = StaffModel.query.get(staff_id)
                room = RoomModel.query.get(room_id)
                staff.serve.append(room)
            db.session.commit()
        else:
            staff_id = data.get('staff_id')
            room_id = data.get('room_id')
            staff = StaffModel.query.get(staff_id)
            room = RoomModel.query.get(room_id)
            staff.serve.append(room)
            db.session.commit()

        return 'add room to staff'

    def delete(self):
        args = staff_room_parser.parse_args()
        staff_id = args.get('staff_id')
        room_id = args.get('room_id')
        print(args)
        if staff_id and room_id:
            staff = StaffModel.query.get(staff_id)
            room = RoomModel.query.get(room_id)
            staff.serve.remove(room)
            db.session.commit()
            return f'delete staff_id {staff_id} and room_id {room_id}'
        elif staff_id:
            staff = StaffModel.query.get(staff_id)
            staff.serve.clear()
            db.session.commit()
            return f'delete staff_id {staff_id}'
        elif room_id:
            room = RoomModel.query.get(room_id)
            room.roomms.clear()
            db.session.commit()
            return f'delete room_id {room_id}'
