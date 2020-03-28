from flask import request
from flask_restful import fields, Resource, marshal_with
from flask_rest_api.staff.staff_obj import Staff
import json


with open('staff/staff_data.json', 'r') as f:
    staff_data_json = json.load(f)

DATA_STAFF = []
for staff in staff_data_json:
    DATA_STAFF.append(
        Staff(
            name=staff.get('name'),
            passport_id=staff.get('passport_id'),
            position=staff.get('position'),
            salary=staff.get('salary')
        )
    )

staff_structure = {
    "name": fields.String,
    "passport_id": fields.String,
    "salary": fields.Float,
    "position": fields.String
}


class StaffList(Resource):
    @marshal_with(staff_structure)
    def get(self):
        return DATA_STAFF

    def patch(self):
        result = request.json
        for staff in DATA_STAFF:
            if staff.passport_id == result['passport_id']:
                staff.name = result.get('name') or staff.name
                staff.position = result.get('position') or staff.name
                staff.salary = result.get('salary') or staff.name
        return 'patch'

class StaffPassport(Resource):
    @marshal_with(staff_structure)
    def get(self, passport_id):
        return [staff for staff in DATA_STAFF if staff.passport_id == passport_id]

    def delete(self, passport_id):
        DATA_STAFF[:] = [staff for staff in DATA_STAFF if staff.passport_id != passport_id]
        return 'delete'

