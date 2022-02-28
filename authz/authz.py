from flask import Flask

from authz.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_onject(Config)
    
    return app
