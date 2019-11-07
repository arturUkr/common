from flask import Blueprint
from flask_restful import Api
from flask_rest_api.tenants.resourse import TenantsList, TenantPassport


api_tenants_bp = Blueprint('tenants', __name__)
api = Api(api_tenants_bp)

api.add_resource(TenantsList, '/tenants')
api.add_resource(TenantPassport, '/tenants/<passport_id>')
