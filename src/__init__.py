from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_principal import Principal
from flask_anticsrf import AntiCsrf
from flask_json import FlaskJSON


app = Flask(__name__)

FlaskJSON(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bounty.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#anti_csrf = AntiCsrf(app)

principals = Principal(app)

import src.controllers  # noqa
import src.headers  # noqa

db.create_all()
