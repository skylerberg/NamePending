from flask import request
from flask_json import as_json
from flask_login import current_user

from .. import app, db
from ..schema import SubmissionSchema
from ..models import Submission, Event
from ..enums import SubmissionStatus, EventTypes
from ..helpers import patch_object


@app.route('/challenges/<int:challenge_id>/submissions')
@as_json
def get_submissions(challenge_id):
    schema = SubmissionSchema()
    submissions = Submission.query.filter(db.and_(
        Submission.user_id == current_user.id,
        Submission.challenge_id == challenge_id
    )).order_by(Submission.created.desc()).all()
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
    submission.status = SubmissionStatus.IN_REVIEW.value
    created_event = Event(
        type=EventTypes.SUBMISSION_CREATED.value,
        submission=submission,
        user_id=current_user.id,
    )
    db.session.add(submission)
    db.session.add(created_event)
    db.session.commit()
    return schema.dump(submission)


@app.route('/challenges/<int:challenge_id>/submissions/<int:submission_id>', methods=['PATCH'])
@as_json
def patch_submission(challenge_id, submission_id):
    schema = SubmissionSchema()
    submission = Submission.query.filter(db.and_(
        Submission.challenge_id == challenge_id,
        Submission.user_id == current_user.id,
        Submission.id == submission_id,
    )).first()
    data = request.get_json()
    attributes = schema.load(data, partial=True)

    if attributes['content'] != submission.content or \
            attributes['title'] != submission.title:
        edited_event = Event(
            type=EventTypes.SUBMISSION_EDITED.value,
            submission_id=submission.id,
            user_id=current_user.id,
        )
        db.session.add(edited_event)
    if attributes['score'] != submission.score:
        score_event = Event(
            type=EventTypes.POINTS_EDITED.value,
            submission_id=submission.id,
            user_id=current_user.id,
        )
        db.session.add(score_event)
    if attributes['status'] != submission.status:
        status_event = Event(
            type=EventTypes.STATUS_CHANGED.value,
            submission_id=submission.id,
            user_id=current_user.id,
        )
        db.session.add(status_event)

    patch_object(submission, attributes)
    db.session.add(submission)
    db.session.commit()
    return schema.dump(submission)
