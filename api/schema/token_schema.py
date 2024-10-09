from api import ma


class TokenSchema(ma.Schema):
    class Meta:
        ordered = True

    access_token = ma.String(dump_only=True)
    refresh_token = ma.String(load_only=True)
