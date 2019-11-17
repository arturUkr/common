from flask_restful import fields
from rooms.structure import room_structure

tenant_structure = {
    "passport_id": fields.Integer,
    "name": fields.String,
    "age": fields.Integer,
    "sex": fields.String,
    "city": fields.String,
    "address": fields.String,
    "rooms": fields.Nested(room_structure)
}
