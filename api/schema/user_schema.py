from api import ma, db
from werkzeug.exceptions import abort
from api.models import User
from marshmallow import validate, validates, ValidationError


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        ordered = True

    id = ma.auto_field(dump_only=True)
    username = ma.auto_field(required=True, validate=validate.Length(min=3, max=64))
    email = ma.auto_field(required=True, validate=[validate.Length(max=128), validate.Email()])
    password = ma.String(required=True, load_only=True, validate=validate.Length(min=3))

    @validates('username')
    def validate_username(self, value):
        select = db.select(User).filter_by(username=value)
        if db.session.execute(select).scalar():
            raise ValidationError('Username already in use.')

    @validates('email')
    def validate_email(self, value):
        select = db.select(User).filter_by(email=value)
        if db.session.execute(select).scalar():
            raise ValidationError('Email is already in use.')

    def handle_error(self, error, data, **kwargs):
        return abort(400, error)
