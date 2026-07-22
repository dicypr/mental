from flask_cors import CORS

def init_cors(app):
    CORS(app, origins=app.config["CORS_ORIGINS"])