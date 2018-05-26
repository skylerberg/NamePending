from flask import request, current_app, session
from flask_json import as_json
from flask_login import login_user, logout_user
from flask_principal import identity_changed, Identity, AnonymousIdentity

from .. import app, db
from ..schema import UserSchema
from ..models import User


@app.route('/login', methods=['POST'])
@as_json
def login():
    # TODO add authentication!!!!!!
    schema = UserSchema()
    data = request.get_json()
    user_data = schema.load(data)
    user = User.query.filter(User.email == user_data['email']).first()
    login_user(user)
    identity_changed.send(current_app._get_current_object(), identity=Identity(user.id))
    return schema.dump(user)


@app.route('/signup', methods=['POST'])
@as_json
def signup():
    # TODO add authentication!!!!!!
    schema = UserSchema()
    data = request.get_json()
    user = User(**schema.load(data))
    db.session.add(user)
    db.session.commit()
    login_user(user)
    identity_changed.send(current_app._get_current_object(), identity=Identity(user.id))
    return schema.dump(user)


@app.route('/logout', methods=['POST'])
@as_json
def logout():
    logout_user()
    for key in ('identity.name', 'identity.auth_type'):
        session.pop(key, None)
    identity_changed.send(current_app._get_current_object(), identity=AnonymousIdentity())
    return {}
