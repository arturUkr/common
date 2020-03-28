from flask import Flask
from flask_rest_api.config import run_config
from flask_rest_api.rooms import api_rooms_bp
from flask_rest_api.tenants import api_tenants_bp
from flask_rest_api.staff import api_staff_bp


app = Flask(__name__)
app.config.from_object(run_config())

app.register_blueprint(api_rooms_bp)
app.register_blueprint(api_tenants_bp)
app.register_blueprint(api_staff_bp)


if __name__ == "__main__":
    app.run()
