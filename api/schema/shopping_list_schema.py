from api import ma
from api.models import ShoppingList
from marshmallow import validate


class ShoppingListSchema(ma.SQLAlchemySchema):
    class Meta:
        model = ShoppingList
        ordered = True

    id = ma.auto_field()
    items = ma.Dict(keys=ma.String(),
                    values=ma.Integer(validate=validate.Range(min=0)),
                    required=True)
