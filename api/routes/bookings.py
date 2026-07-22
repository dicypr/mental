from flask import Blueprint, request
from flask_login import current_user, login_required
from api import db
from api.models import User, Appointments
from api.schemas import user_schema, appointments_schema
from api.utils.response import (
    success_response,
    error_response,
    validation_error_response,
)
from marshmallow import ValidationError

bookings = Blueprint("bookings", __name__)

#
# @bookings.route("/bookings", methods=["POST"])
# @login_required
# def bookings():
#     bookings = db.session.execute(
#         db.select(Appointments).filter_by(customer_id=current_user.id)
#     ).fetchall()
#     result = {}
#     n = 0
#
#     for booking in bookings:
#         n += 1
#         result[n] = appointments_schema.dump(booking[0])
#
#     return success_response(result)
