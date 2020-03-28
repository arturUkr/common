from flask import Blueprint
from flask_restful import Api

from tenants.resource import TenantsList#, TenantPassport

tenant_bp = Blueprint('tenant', __name__)
api = Api(tenant_bp)


api.add_resource(TenantsList, '/tenants', "/tenants/<int:passport_id>")
# api.add_resource(TenantPassport, '/tenants/<passport_id>')
