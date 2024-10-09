from flask import Blueprint

bp = Blueprint(
    'tokens',
    __name__,
    url_prefix='/api/tokens',
)

from api.tokens import routes
