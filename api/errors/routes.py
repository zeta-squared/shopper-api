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
    if hasattr(error.description, 'messages_dict'):
        messages = {}
        for key in error.description.messages_dict:
            messages[key] = error.description.messages_dict[key][0]
        return {
                'code': error.code,
                'name': error.name,
                'description': error.description,
                'messages': messages if error.description.messages_dict else None
                }
    else:
        return error


@bp.app_errorhandler(401)
@response(ErrorSchema, status_code=401)
def unauthorised(error):
    return error
