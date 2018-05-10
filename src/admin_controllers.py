from flask import request
from flask_json import as_json

from . import app, db
from .schema import ChallengeSchema, SubmissionSchema
from .models import Challenge, Submission


@app.route('/admin/challenges', methods=['POST'])
@as_json
def admin_post_challenge():
    schema = ChallengeSchema()
    data = request.get_json()
    challenge = Challenge(**schema.load(data))
    session = db.session()
    session.add(challenge)
    session.commit()
    return schema.dump(challenge)


@app.route('/admin/challenges/<int:challenge_id>/submissions')
@as_json
def admin_get_submissions(challenge_id):
    schema = SubmissionSchema()
    submissions = Submission.query.filter(db.and_(
        Submission.challenge_id == challenge_id
    )).all()
    return schema.dump(submissions, many=True)


@app.route('/admin/challenges/<int:challenge_id>/submissions/<int:submission_id>')
@as_json
def admin_get_submission(challenge_id, submission_id):
    schema = SubmissionSchema()
    submission = Submission.query.filter(db.and_(
        Submission.challenge_id == challenge_id,
        Submission.id == submission_id,
    )).first()
    return schema.dump(submission)


def admin_get_comments():
    pass


def admin_post_comment():
    pass


def admin_get_comments():
    pass
