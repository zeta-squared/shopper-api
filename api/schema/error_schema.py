from api import ma


class ErrorSchema(ma.Schema):
    class Meta:
        ordered = True

    code = ma.Integer()
    name = ma.String()
    description = ma.String()
    messages = ma.Dict()
