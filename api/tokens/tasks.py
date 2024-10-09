import jwt
from api import db
from datetime import datetime, timezone, timedelta
from flask import current_app, url_for
from werkzeug.http import dump_cookie


def token_response(token):
    headers = {}
    samesite = 'none' if not current_app.debug else 'lax'
    headers['Set-Cookie'] = dump_cookie(
        'refresh_token', token.refresh_token,
        path=url_for('tokens.issue_token'), secure=not current_app.debug,
        httponly=True, samesite=samesite)

    return {'access_token': token.access_token_jwt, 'refresh_token': None}, 200, headers


def clear_refresh_token():
    expires = datetime.now(timezone.utc) - timedelta(minutes=1)
    headers = {
        'Set-Cookie': dump_cookie('refresh_token', expires=expires),
    }
    return headers


def delete_token(token):
    db.session.delete(token)
    db.session.commit()
    return
