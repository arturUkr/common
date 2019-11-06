from flask import Flask
from flask_restful import Api
from flask_rest_api.config import run_config

from flask_rest_api.rooms import api_rooms_bp

app = Flask(__name__)
app.config.from_object(run_config())
app.register_blueprint(api_rooms_bp)


if __name__ == "__main__":
    app.run()
