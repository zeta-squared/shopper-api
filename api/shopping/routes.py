from api import db
from api.shopping import bp
from apifairy import body, authenticate, response, other_responses
from api.models import ShoppingList
from api.schema import ShoppingListSchema, ErrorSchema
from api.auth import token_auth


@bp.route('', methods=['GET'])
@authenticate(token_auth)
@response(ShoppingListSchema)
@other_responses({
    401: (ErrorSchema, 'Invalid access token'),
    404: (ErrorSchema, 'Shopping list not found'),
})
def get_shopping_list():
    """
    Get a user's shopping list
    """
    user = token_auth.current_user()
    shopping_list = db.session.execute(user.shopping_list.select()).scalar()
    return shopping_list or abort(404)


@bp.route('', methods=['POST'])
@body(ShoppingListSchema)
@authenticate(token_auth)
@response(ShoppingListSchema)
@other_responses({
    201: (ShoppingListSchema, 'Created'),
    401: (ErrorSchema, 'Invalid access token')
})
def update_shopping_list(args):
    """
    Create or update a user's shopping list
    """
    user = token_auth.current_user()
    shopping_list = db.session.execute(user.shopping_list.select()).scalar()
    if not shopping_list:
        shopping_list = ShoppingList(items=args.get('items'), user=user)
        db.session.add(shopping_list)
        db.session.commit()
        return shopping_list, 201

    shopping_list.items = args.get('items')
    db.session.commit()

    return shopping_list
