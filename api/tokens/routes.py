import threading
from api import db
from flask import request
from api.tokens import bp
from apifairy import authenticate, response, other_responses, body
from api.schema import TokenSchema, ErrorSchema, EmptySchema
from api.auth import basic_auth, token_auth, refresh_auth
from api.tokens.tasks import token_response, clear_refresh_token, delete_token
from api.models import Token


@bp.route('', methods=['POST'])
@authenticate(basic_auth)
@response(TokenSchema)
@other_responses({401: (ErrorSchema, 'Invalid username or password')})
def issue_token():
    """
    Issue a new access and refresh token

    Returns an access token and refresh token. The access token has a duration of 15 minutes.
    The refresh token is sent as a secure HTTP cookie to reduce the likelihood of cross-site
    scripting.
    """
    user = basic_auth.current_user()
    token = user.generate_token()
    db.session.add(token)
    db.session.commit()
    return token_response(token)


@bp.route('', methods=['PUT'])
@body(TokenSchema)
@authenticate(refresh_auth)
@response(TokenSchema)
@other_responses({401: (ErrorSchema, 'Invalid access or refresh token')})
def refresh_token(args):
    """
    Refresh an access token

    The user's current access token must be sent as a bearer authorisation token. The current
    refresh token is to be sent in either the body of the request or a cookie. If an expired
    refresh token is used, all user tokens will be revoked for security purposes. The response
    follows the same format as when a new access and refresh token are issued.
    """
    access_token_jwt = request.headers['Authorization'].split()[1]
    token = Token.from_jwt(access_token_jwt)
    db.session.delete(token)
    token = refresh_auth.current_user().generate_token()
    db.session.add(token)
    db.session.commit()
    return token_response(token)


@bp.route('', methods=['DELETE'])
@authenticate(token_auth)
@response(EmptySchema, description='Token successfully revoked')
@other_responses({401: (ErrorSchema, 'Invalid access token'),
                  400: (ErrorSchema, 'Bad Request - ensure you have sent the complete token string')})
def revoke_token():
    """
    Revoke an access token
    """
    access_token_jwt = request.headers['Authorization'].split()[1]
    token = Token.from_jwt(access_token_jwt)
    db.session.delete(token)
    db.session.commit()
    return
