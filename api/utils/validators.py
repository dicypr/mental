import re
from marshmallow import ValidationError


def validate_password(password):
    # Validate password strength

    if len(password) < 8:
        raise ValidationError("Password must be at least 8 characters")
    if not re.search(r"[A-Z]", password):
        raise ValidationError("Password must contain at least one uppercase letter.")
    if not re.search(r"[a-z]", password):
        raise ValidationError("Password must contain at least one lowercase letter.")
    if not re.search(r"[0-9]", password):
        raise ValidationError("Password must contain at least one number")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        raise ValidationError("Password must contain at least one special character")


def validate_username(username):
    # Validate username format

    if not re.match(r"^[a-zA-Z0-9_]+$", username):
        raise ValidationError(
            "Username must contain only letters, numbers and underscore"
        )
    if len(username) < 3:
        raise ValidationError("Username must be at least 3 characters")
    if len(username) > 30:
        raise ValidationError("Username must be at most 30 characters")


def validate_email(email):
    # Validate email format
    if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
        raise ValidationError("Invalid email format.")
