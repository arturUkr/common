from flask import request
from flask_restful import Resource, marshal_with
from db import db
from models import TenantModel
from tenants.structure import tenant_structure


class TenantsList(Resource):
    @marshal_with(tenant_structure)
    def get(self, passport_id=None):
        model_obj = TenantModel.query
        return model_obj.get(passport_id) if passport_id else model_obj.all()

    def post(self):
        if isinstance(request.json, list):
            for tenant in request.json:
                new_tenant = TenantModel(**tenant)
                db.session.add(new_tenant)
                db.session.commit()
        else:
            new_tenant = TenantModel(**request.json)
            db.session.add(new_tenant)
            db.session.commit()
        return 'create new tenant'

    def patch(self, passport_id=None):
        if passport_id:
            new_data = request.json
            old_data = TenantModel.query.get(passport_id)

            old_data.name = new_data.get('name')
            old_data.age = new_data.get('age')
            old_data.sex = new_data.get('sex')
            old_data.address = new_data.get('address')
            # old_data.room_number = new_data.get('room_number')

            db.session.commit()
            return 'update data'
        else:
            return 'need /tenants/<int:passport_id>'

    def delete(self, passport_id=None):
        if passport_id:
            data = TenantModel.query.get(passport_id)
            db.session.delete(data)
            db.session.commit()
            return f'delete tenant {data.passport_id}'
        else:
            return 'need /tenants/<int:passport_id>'
