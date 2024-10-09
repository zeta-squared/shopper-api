import threading
from api import db
from flask import abort, request
from datetime import datetime, timezone
from flask_httpauth import HTTPTokenAuth
from api.models import Token
from api.auth import token_auth

refresh_auth = HTTPTokenAuth()


@refresh_auth.verify_token
def verify_token(access_token_jwt):
    token = Token.from_jwt(access_token_jwt)
    if token:
        if not (refresh_token := request.cookies.get('refresh_token')):
            refresh_token = request.json.get('refresh_token')
        naive_now = datetime.now(timezone.utc).replace(tzinfo=None)
        if token.refresh_token == refresh_token and token.refresh_expiration > naive_now:
            return token.user
        elif token.refresh_expiration > naive_now:
            return abort(401, 'Invalid refresh token')

        db.session.execute(db.delete(Token).where(Token.user_id==token.user.id))
        return abort(401, 'Expired refresh token, all user tokens have been revoked')

    return abort(401, 'Invalid access token')
