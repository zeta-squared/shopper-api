from api import db
from flask import abort
from datetime import datetime, timezone
from flask_httpauth import HTTPTokenAuth
from api.models import Token

token_auth = HTTPTokenAuth()


@token_auth.verify_token
def verify_token(access_token_jwt):
    token = Token.from_jwt(access_token_jwt)
    if token and token.access_expiration > datetime.now(timezone.utc).replace(tzinfo=None):
        return token.user

    return abort(401, 'Invalid access token')
