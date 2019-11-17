from flask_restful import fields
from rooms.structure import room_structure

staff_structure = {
    "passport_id": fields.Integer,
    "name": fields.String,
    "position": fields.String,
    "salary": fields.Float,
    "serve": fields.Nested(room_structure)
}

staff_room_structure = {
    # "number": fields.Nested(room_structure),
    "passport_id": fields.Nested(staff_structure)#fields.Integer
}
