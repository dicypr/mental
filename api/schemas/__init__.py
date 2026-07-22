from sqlalchemy.orm import load_only
from api import ma
from marshmallow import fields, validate, pre_load
from api.models import User, Appointments, Condition, Goals, Resource


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

    id = ma.auto_field(dump_only=True)
    username = ma.auto_field(dump_only=True, validate=validate.Length(min=3, max=80))
    email = ma.auto_field(required=True, validate=validate.Email())
    password_hash = ma.auto_field(
        required=True, load_only=True, validate=validate.Length(min=8, max=80)
    )
    created_at = ma.auto_field(dump_only=True)
    # points = ma.auto_field(dump_only=True)

    @pre_load
    def process_password(self, data, **kwargs):
        if "password" in data:
            data["password"] = data["password"].strip()
        return data


class AppointmentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Appointments
        load_instance = True

    id = ma.auto_field(dump_only=True)
    timeslot = ma.auto_field(required=True)
    problem = ma.auto_field(required=True)
    # customer_id = ma.auto_field(dump_only=True)
    # customer = fields.Nested(UserSchema, only=("id", "username"), dump_only=True)


class ResourceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Resource
        load_instance = True

    id = ma.auto_field(dump_only=True)
    name = ma.auto_field(required=True)
    link = ma.auto_field(required=True)
    # condition_id = ma.auto_field()
    # condition = fields.Nested(ConditionSchema, only=("id", "name"), dump_only=True)


class ConditionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Condition
        load_instance = True

    id = ma.auto_field(dump_only=True)
    name = ma.auto_field(required=True)
    desc = ma.auto_field(required=True)
    # resources = fields.Nested(ResourceSchema, only=("id", "name", "link"), many=True)


class GoalsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Goals
        load_instance = True

    id = ma.auto_field(dump_only=True)
    # user_id = ma.auto_field()
    goal_name = ma.auto_field(required=True)
    goal_description = ma.auto_field()
    target = ma.auto_field(required=True)
    goal_points = ma.auto_field()

    # user = fields.Nested(UserSchema, only=("id", "username", "points"), dump_only=True)


class LoginSchema(ma.Schema):
    username = fields.String()
    email = fields.String(required=True)
    password = fields.String(required=True, load_only=True)


user_schema = UserSchema()
appointments_schema = AppointmentSchema()
resource_schema = ResourceSchema()
condition_schema = ConditionSchema()
goal_schema = GoalsSchema()
login_schema = LoginSchema()
