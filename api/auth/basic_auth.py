from api import db
from flask import abort
from flask_httpauth import HTTPBasicAuth
from api.models import User

basic_auth = HTTPBasicAuth()


@basic_auth.verify_password
def verify_password(username, password):
    if username and password:
        select = db.select(User).filter_by(username=username)
        user = db.session.execute(select).scalar()
        if user and user.verify_password(password):
            return user

    return abort(401)
