from api import create_app, db
from api.models import User

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'User': User}
