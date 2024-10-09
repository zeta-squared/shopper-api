from api import db
from typing import Optional
from sqlalchemy.orm import Mapped, WriteOnlyMapped, mapped_column


class ShoppingList(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    items: Mapped[Optional[dict[str, int]]] = mapped_column(db.PickleType)

    user_id: Mapped[int] = mapped_column(db.ForeignKey('user.id'), index=True)
    user: Mapped['User'] = db.relationship(back_populates='shopping_list')

    def __repr__(self):
        return "<{}'s shopping list>".format(self.user.username)
