from flask import Blueprint

bp = Blueprint(
    'users',
    __name__,
    url_prefix='/api/users',
)

from api.users import routes
