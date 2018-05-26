from flask import request
from flask_json import as_json

from .. import app, db
from ..schema import ChallengeSchema
from ..models import Challenge


@app.route('/challenges/<int:challenge_id>')
@as_json
def get_challenge(challenge_id):
    schema = ChallengeSchema()
    challenge = Challenge.query.filter(Challenge.id == challenge_id).first()
    return schema.dump(challenge)


@app.route('/challenges', methods=['POST'])
@as_json
def post_challenge():
    schema = ChallengeSchema()
    data = request.get_json()
    challenge = Challenge(**schema.load(data))
    db.session.add(challenge)
    db.session.commit()
    return schema.dump(challenge)
