from flask import Blueprint
from flask_restful import Api
from flask_rest_api.staff.resource import StaffList, StaffPassport

api_staff_bp = Blueprint('staff', __name__)
api = Api(api_staff_bp)


api.add_resource(StaffList, '/staff')
api.add_resource(StaffPassport, '/staff/<passport_id>')
