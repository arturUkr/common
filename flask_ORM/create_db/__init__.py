from flask import Blueprint
from flask_restful import Api

from create_db.resource import WorkWithDB

create_db_bp = Blueprint('create_db', __name__)
api = Api(create_db_bp)


api.add_resource(WorkWithDB, '/work_with_db')
