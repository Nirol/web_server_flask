from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from config import config

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    #TODO: change location of this setting to env
    app.config['SECRET_KEY'] = 'hard to guess string'

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)
    csrf = CSRFProtect(app)
    db.init_app(app)
    # USED TO CREATE TABLES
    with app.app_context():
        db.create_all()
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/')
    return app
