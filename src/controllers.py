from flask import request, current_app
from flask_json import as_json
from flask_login import current_user, login_user
from flask_principal import identity_changed, Identity

from . import app, db
from .schema import ChallengeSchema, CommentSchema, SubmissionSchema, UserSchema
from .models import Challenge, Comment, Submission, User
from .permissions import SubmissionOwnerPermission


@app.route('/login', methods=['POST'])
@as_json
def login():
    # TODO add authentication!!!!!!
    schema = UserSchema()
    data = request.get_json()
    user_data = schema.load(data)
    user = User.query.filter(User.email == user_data['email']).first()
    print(user)
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
    session = db.session()
    session.add(user)
    session.commit()
    login_user(user)
    identity_changed.send(current_app._get_current_object(), identity=Identity(user.id))
    return schema.dump(user)


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


@app.route('/challenges/<int:challenge_id>/submissions')
@as_json
def get_submissions(challenge_id):
    schema = SubmissionSchema()
    submissions = Submission.query.filter(db.and_(
        Submission.user_id == current_user.id,
        Submission.challenge_id == challenge_id
    )).all()
    return schema.dump(submissions, many=True)


@app.route('/challenges/<int:challenge_id>/submissions/<int:submission_id>')
@as_json
def get_submission(challenge_id, submission_id):
    schema = SubmissionSchema()
    submission = Submission.query.filter(db.and_(
        Submission.challenge_id == challenge_id,
        Submission.user_id == current_user.id,
        Submission.id == submission_id,
    )).first()
    return schema.dump(submission)


@app.route('/challenges/<int:challenge_id>/submissions', methods=['POST'])
@as_json
def post_submission(challenge_id):
    schema = SubmissionSchema()
    data = request.get_json()
    submission = Submission(**schema.load(data))
    submission.challenge_id = challenge_id
    submission.user_id = current_user.id
    session = db.session()
    session.add(submission)
    session.commit()
    return schema.dump(submission)


@app.route('/challenges/<int:challenge_id>/submissions/<int:submission_id>/comments')
@as_json
def get_comments(challenge_id, submission_id, comment_id):
    SubmissionOwnerPermission(submission_id).test()
    schema = CommentSchema()
    comments = Comment.query.filter(Comment.submission_id == submission_id).all()
    return schema.dump(comments, many=True)


@app.route('/challenges/<int:challenge_id>/submissions/<int:submission_id>/comments', methods=['POST'])
@as_json
def post_comment(challenge_id, submission_id):
    SubmissionOwnerPermission(submission_id).test()
    schema = CommentSchema()
    data = request.get_json()
    comment = Comment(**schema.load(data))
    comment.submission_id = submission_id
    comment.user_id = current_user.id
    session = db.session()
    session.add(comment)
    session.commit()
    return schema.dump(comment)
