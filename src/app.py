from flask import Flask
from api import api


def create_app():
    """ 
    Creates a Flask app. 
    Registers a blueprint for our api. 
    Returns the Flask app.
    """
    app = Flask(__name__)
    app.register_blueprint(api)
    return app