from flask import Blueprint

bp = Blueprint(
    'errors',
    __name__,
    url_prefix='/api',
)

from api.errors import routes
