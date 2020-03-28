from pprint import pprint

from flask import request
from flask_rest_api.tenants.tenant_obj import Tenants
import json
from flask_restful import fields, Resource, marshal_with


with open('tenants/tenants_data.json', 'r') as f:
    data_tenants_json = json.load(f)

DATA_TENANTS = []
for tenant in data_tenants_json:
    DATA_TENANTS.append(
        Tenants(name=tenant.get('name'),
                passport_id=tenant.get('passport_id'),
                age=tenant.get('age'),
                sex=tenant.get('sex'),
                address=tenant.get('address'),
                room_number=tenant.get('room_number'))
    )


tenant_structure = {
    "name": fields.String,
    "passport_id": fields.String,
    "age": fields.Integer,
    "sex": fields.String,
    "address": fields.Nested({
        "city": fields.String,
        "street": fields.String
    }),
    "room_number": fields.Integer
  }


class TenantsList(Resource):
    @marshal_with(tenant_structure)
    def get(self):
        return DATA_TENANTS

    def patch(self):
        result = request.json
        for tenant in DATA_TENANTS:
            if tenant.passport_id == result['passport_id']:
                tenant.name = result.get('name') or tenant.name
                tenant.age = result.get('age') or tenant.name
                tenant.sex = result.get('sex') or tenant.name
                tenant.address = result.get('address') or tenant.name
                tenant.room_number = result.get('room_number') or tenant.name

        return 'patch'


class TenantPassport(Resource):
    @marshal_with(tenant_structure)
    def get(self, passport_id):
        return [tenant for tenant in DATA_TENANTS if tenant.passport_id == passport_id]

    def delete(self, passport_id):
        DATA_TENANTS[:] = [tenant for tenant in DATA_TENANTS if tenant.passport_id != passport_id]
        return 'delete'
