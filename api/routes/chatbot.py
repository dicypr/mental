from flask import Blueprint, request
from api.utils.response import success_response, error_response
from api.gemini import *

bot_bp = Blueprint("chatbot", __name__)


@bot_bp.route("/chatbot", methods=["POST", "OPTIONS"])
def chatbot():
    try:
        data = request.get_json()
        if not data:
            return error_response("Enter a prompt", 400)

        output = get_response(data["prompt"])

        return success_response(output)
    except Exception as e:
        return error_response(str(e), 500)
