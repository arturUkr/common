from flask import Blueprint
from flask_restful import Api
from staff.resource import StaffList, RoomStaff


staff_bp = Blueprint('satff', __name__)
api = Api(staff_bp)


api.add_resource(StaffList, '/staff', '/staff/<int:passport_id>')
api.add_resource(RoomStaff, '/room_staff')
# api.add_resource(RoomStaffByRoom, '/room_staff/room/<int:room_id>')
