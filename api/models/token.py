import secrets
import jwt
from jwt.exceptions import DecodeError
from api import db
from flask import current_app, abort
from datetime import datetime, timezone, timedelta
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Token(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    access_token: Mapped[str] = mapped_column(db.String(64), index=True)
    access_expiration: Mapped[datetime]
    refresh_token: Mapped[str] = mapped_column(db.String(64), index=True)
    refresh_expiration: Mapped[datetime]

    user_id: Mapped[int] = mapped_column(db.ForeignKey('user.id'), index=True)
    user: Mapped['User'] = db.relationship(back_populates='token')

    def __repr__(self):
        return '<Token for {}'.format(self.user.username)

    @property
    def access_token_jwt(self):
        return jwt.encode({'access_token': self.access_token},
                          current_app.config['SECRET_KEY'], algorithm='HS256')

    def generate(self):
        self.access_token = secrets.token_urlsafe()
        self.access_expiration = datetime.now(timezone.utc) + \
                timedelta(minutes=current_app.config['ACCESS_TOKEN_DURATION'])
        self.refresh_token = secrets.token_urlsafe()
        self.refresh_expiration = datetime.now(timezone.utc) + \
                timedelta(days=current_app.config['REFRESH_TOKEN_DURATION'])

    @staticmethod
    def from_jwt(access_token_jwt):
        try:
            access_token = jwt.decode(
                access_token_jwt, current_app.config['SECRET_KEY'], algorithms=['HS256']
            )['access_token']
            token = db.session.execute(
                db.select(Token).filter_by(access_token=access_token)
            ).scalar()
            return token or None
        except DecodeError:
            return abort(400)
