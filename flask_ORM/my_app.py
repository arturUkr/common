from flask import Flask

from config import run_config
from db import db

from create_db import create_db_bp
from tenants import tenant_bp
from rooms import room_bp
from staff import staff_bp


def create_app():

    app = Flask(__name__)
    app.config.from_object(run_config())

    db.init_app(app)

    app.register_blueprint(create_db_bp)
    app.register_blueprint(tenant_bp)
    app.register_blueprint(room_bp)
    app.register_blueprint(staff_bp)

    return app


if __name__ == '__main__':
    create_app().run()
