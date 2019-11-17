from flask_restful import fields

room_structure = {
    "number": fields.Integer,
    "level": fields.Integer,
    "status": fields.String,
    "price": fields.Float,
    "tenant_id": fields.Integer
}