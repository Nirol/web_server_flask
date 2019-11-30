from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
moment = Moment(app)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'hard to guess string'

username = "root"
passs = "4834calbon"
host = "127.0.0.1/"
db_name = "flasky"
full_db_url = 'mysql://' + username + ":" + passs + "@" + host + db_name
app.config['SQLALCHEMY_DATABASE_URI'] = full_db_url
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)