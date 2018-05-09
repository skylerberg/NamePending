from flask import request
from flask_json import as_json


from . import app, db
from .schema import ChallengeSchema, CommentSchema, SubmissionSchema, UserSchema
from .models import Challenge, Comment, Submission, User


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
    session = db.session()
    session.add(challenge)
    session.commit()
    return schema.dump(challenge)


@app.route('/challenges/<int:challenge_id>/submissions/<int:submission_id>')
@as_json
def get_submission(challenge_id, submission_id):
    pass


@app.route('/challenges/<int:challenge_id>/submissions/<int:submission_id>/comments/<int:comment_id>')
def get_comment(challenge_id, submission_id, comment_id):
    pass


@app.route('/users/<int:user_id>')
def get_user(user_id):
    pass
