from os import error
from flask import Blueprint, request
from flask_login import login_user, logout_user, login_required, current_user
import functools
from api import db
from api.models import User
from api.schemas import user_schema, login_schema
from api.utils.validators import validate_username, validate_password
from api.utils.response import (
    success_response,
    error_response,
    validation_error_response,
)
from marshmallow import ValidationError, validate

auth_bp = Blueprint("auth", __name__)

#
# @auth_bp.route("/register", methods=["GET", "POST"])
# def register():
#     try:
#         # get data from the request
#         data = request.get_json()
#
#         # if data is not found
#         if not data:
#             return error_response("No data provided", 400)
#
#         # validate input
#         validated_data = login_schema.load(data)
#
#         validate_password(validated_data["password"])
#         validate_username(validated_data["username"])
#
#         # checking if the user already exists
#         if User.query.filter_by(email=validated_data["email"]).first():
#             return error_response("User with this email already exists", 409)
#         if User.query.filter_by(username=validated_data["username"]).first():
#             return error_response("User with this username already exists", 409)
#
#         # create new user
#         new_user = User(
#             username=validated_data.get(
#                 "username", validated_data["email"].split("@")[0]
#             ),
#             email=validated_data["email"],
#         )
#
#         new_user.set_password(validated_data["password"])
#
#         db.session.add(new_user)
#         db.session.commit()
#
#         login_user(new_user)
#
#         return success_response(user_schema.dump(new_user), 201)
#     except ValidationError as err:
#         return validation_error_response(err.messages)
#     except Exception as e:
#         db.session.rollback()
#         return error_response(f"{e}Registration failed", 500)
#
#
# @auth_bp.route("/login", methods=["POST"])
# def login():
#     try:
#         data = request.get_json()
#         if not data:
#             return error_response("No data provided", 400)
#
#         validated_data = login_schema.load(data)
#
#         user = User.query.filter_by(email=validated_data["email"]).first()
#
#         if user and user.check_password(validated_data["password"]):
#             login_user(user, remember=True)
#             return success_response(user_schema.dump(user))
#
#         return error_response("Invalid email or password", 401)
#     except ValidationError as err:
#         return validation_error_response(err.messages)
#
#
# @auth_bp.route("/logout", methods=["POST"])
# @login_required
# def logout():
#     logout_user()
#     return success_response(None, "Logout successful")
#
#
# @auth_bp.route("/check-auth", methods=["GET"])
# @login_required
# def check_auth():
#     return success_response(user_schema.dump(current_user))
#
#
# @auth_bp.route("/profile", methods=["GET"])
# @login_required
# def get_profile():
#     return success_response(user_schema.dump(current_user))
#
#
# # @auth_bp.route("/update-profile", methods=["PUT"])
# # @login_required
# # def update_profile():
# #     try:
# #         data = request.get_json()
# #
# #         if "username" in data:
# #             validate_username(data["username"])
# #             if User.query.filter_by(
# #                 username = data["username"], id != current_user.id
# #             ).first():
# #                 return error_response("Username already taken", 409)
# #             current_user.username = data["username"]
# #
# #         if "email" in data:
# #             if User.query.filter(
# #                 email=data["email"], id != current_user.id
# #             ).first():
# #                 return error_response("Email already in use", 409)
# #             current_user.email = data["email"]
# #
# #         db.session.commit()
# #         return success_response(user_schema.dump(current_user))
# #     except ValidationError as err:
# #         return validation_error_response(err.messages)
