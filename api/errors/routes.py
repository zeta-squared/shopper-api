from api.errors import bp
from api.schema import ErrorSchema
from flask import Blueprint
from apifairy import response


@bp.app_errorhandler(404)
@response(ErrorSchema, status_code=404)
def not_found(error):
    return error


@bp.app_errorhandler(400)
@response(ErrorSchema, status_code=400)
def bad_request(error):
    return error


@bp.app_errorhandler(401)
@response(ErrorSchema, status_code=401)
def unauthorised(error):
    return error
