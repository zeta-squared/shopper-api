from config import Config
from flask import Flask, redirect, url_for
from flask_cors import CORS
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase
from apifairy import APIFairy

convention = {
    'ix': 'ix_%(column_0_label)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(constraint_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'pk': 'pk_%(table_name)s'
}

class Base(DeclarativeBase):
    metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(model_class=Base)
ma = Marshmallow()
cors = CORS()
migrate = Migrate()
apifairy = APIFairy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    ma.init_app(app)
    cors.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    apifairy.init_app(app)

    # Register blueprints
    from api.users import bp as users_bp
    app.register_blueprint(users_bp)

    from api.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from api.tokens import bp as tokens_bp
    app.register_blueprint(tokens_bp)

    from api.shopping import bp as shopping_bp
    app.register_blueprint(shopping_bp)

    # Default route to docs
    @app.route('/')
    def docs():
        return redirect(url_for('apifairy.docs'))

    return app
