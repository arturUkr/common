from flask_restful import Resource
from db import db


class WorkWithDB(Resource):

    def post(self):
        db.create_all()
        db.session.commit()
        return 'create database'
