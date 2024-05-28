from flask import Flask
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint
from .routes import register_routes

def create_app():
    app = Flask(__name__)
    api = Api(app)

    # Register routes
    register_routes(api)

    # Swagger setup
    SWAGGER_URL = '/api/docs'
    API_URL = '/static/swagger.json'
    swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "Vitivinicultura API"})
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    return app
