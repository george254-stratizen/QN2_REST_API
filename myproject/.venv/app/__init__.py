from flask import Flask

def create_app():
    app = Flask(__name__)

    # Register routes
    from .routes import api_blueprint
    app.register_blueprint(api_blueprint)

    return app
