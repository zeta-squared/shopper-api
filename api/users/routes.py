from flask import abort, url_for
from api import db
from api.users import bp
from api.models import User
from api.schema import UserSchema, ErrorSchema
from api.auth import token_auth
from apifairy import body, response, other_responses, authenticate


@bp.route('/<string:username>', methods=['GET'])
@response(UserSchema)
@other_responses({404: (ErrorSchema, 'User not found')})
def get_users(username):
    """
    Retrieve a user by username
    """
    select = db.select(User).filter_by(username=username)
    user = db.session.execute(select).scalar()
    return user or abort(404)


@bp.route('', methods=['POST'])
@body(UserSchema)
@response(UserSchema, 201)
@other_responses({400: ErrorSchema})
def register_user(user):
    """
    Register a new user
    """
    user = User(**user)
    db.session.add(user)
    db.session.commit()
    return user


@bp.route('/me', methods=['GET'])
@authenticate(token_auth)
@response(UserSchema)
@other_responses({401: ErrorSchema})
def me():
    """
    Retrieve authenticated user information
    """
    return token_auth.current_user()
