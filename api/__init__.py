import os

from flask import Flask, render_template_string
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()

db = SQLAlchemy()
login_manager = LoginManager()
ma = Marshmallow()


def create_app():
    app = Flask(__name__)

    CORS(app)

    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY") or "secret-key"

    login_manager.init_app(app)
    ma.init_app(app)

    from api.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from api.routes.auth import auth_bp
    app.register_blueprint(auth_bp)

    from api.routes.chatbot import bot_bp
    app.register_blueprint(bot_bp)

    @app.route("/", methods=["GET"])
    @app.route("/api/index.py", methods=["GET"])
    def home():
        template_paths = [
            os.path.join(os.path.dirname(__file__), "..", "templates", "index.html"),
            os.path.join(os.path.dirname(__file__), "templates", "index.html"),
        ]
        for path in template_paths:
            if os.path.exists(path):
                with open(path, "r", encoding="utf-8") as f:
                    return render_template_string(f.read())
        return {
            "status": "success",
            "message": "Mental Health Chatbot API is running!",
            "endpoints": {
                "chatbot": "POST /chatbot"
            }
        }, 200

    return app
