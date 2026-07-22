from flask import Blueprint, request
from api.utils.response import success_response, error_response
from api.gemini import *

bot_bp = Blueprint("chatbot", __name__)


@bot_bp.route("/chatbot", methods=["GET", "POST", "OPTIONS"])
def chatbot():
    if request.method == "GET":
        return success_response({"message": "Send a POST request with {'prompt': 'your question'} to chat."})
    try:
        data = request.get_json()
        if not data or "prompt" not in data:
            return error_response("Enter a prompt", 400)

        output = get_response(data["prompt"])

        return success_response(output)
    except Exception as e:
        return error_response(str(e), 500)

