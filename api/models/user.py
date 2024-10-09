from api import db
from hashlib import md5
from typing import Optional
from api.models import Token
from sqlalchemy.orm import Mapped, WriteOnlyMapped, mapped_column
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(db.String(64), index=True, unique=True)
    email: Mapped[str] = mapped_column(db.String(128), index=True, unique=True)
    _password_hash: Mapped[Optional[str]] = mapped_column(db.String(256))

    token: WriteOnlyMapped['Token'] = db.relationship(back_populates='user')
    shopping_list: WriteOnlyMapped['ShoppingList'] = db.relationship(back_populates='user')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    @property
    def avatar_url(self):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return f'https://www.gravatar.com/avatar/{digest}?d=identicon'

    @property
    def password(self):
        return self._password_hash

    @password.setter
    def password(self, password):
        self._password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)

    def generate_token(self):
        token = Token(user=self)
        token.generate()
        return token
