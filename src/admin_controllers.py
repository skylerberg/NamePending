from datetime import datetime

from flask import request
from flask_json import as_json
from flask_login import current_user

from . import app, db
from .schema import ChallengeSchema, SubmissionSchema, PointsSchema
from .models import Challenge, Submission, Points


@app.route('/admin/challenges', methods=['POST'])
@as_json
def admin_post_challenge():
    schema = ChallengeSchema()
    data = request.get_json()
    challenge = Challenge(**schema.load(data))
    db.session.add(challenge)
    db.session.commit()
    return schema.dump(challenge)


@app.route('/admin/challenges/<int:challenge_id>/submissions')
@as_json
def admin_get_submissions(challenge_id):
    schema = SubmissionSchema()
    submissions = Submission.query.filter(db.and_(
        Submission.challenge_id == challenge_id
    )).order_by(Submission.created.desc()).all()
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


@app.route('/admin/challenges/<int:challenge_id>/submissions/<int:submission_id>/points', methods=['POST'])
def admin_award_points(challenge_id, submission_id):
    schema = PointsSchema
    data = request.get_json()
    points = Points(**schema.load(data))
    points.submission_id = submission_id
    points.granted_by_id = current_user.id
    points.created = datetime.utcnow()
    db.session.add(points)
    db.session.commit()
    return schema.dump(points)
