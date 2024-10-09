from flask import Blueprint

bp = Blueprint(
    'shopping',
    __name__,
    url_prefix='/api/shopping',
)

from api.shopping import routes
