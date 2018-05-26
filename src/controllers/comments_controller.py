from flask import request
from flask_json import as_json
from flask_login import current_user

from .. import app, db
from ..schema import CommentSchema
from ..models import Comment, Event
from ..enums import EventTypes


@app.route('/challenges/<int:challenge_id>/submissions/<int:submission_id>/comments')
@as_json
def get_comments(challenge_id, submission_id):
    #SubmissionOwnerPermission(submission_id).test()
    schema = CommentSchema()
    comments = Comment.query.filter(
        Comment.submission_id == submission_id
    ).order_by(Comment.created).all()
    return schema.dump(comments, many=True)


@app.route('/challenges/<int:challenge_id>/submissions/<int:submission_id>/comments', methods=['POST'])
@as_json
def post_comment(challenge_id, submission_id):
    #SubmissionOwnerPermission(submission_id).test()
    schema = CommentSchema()
    data = request.get_json()
    comment = Comment(**schema.load(data))
    event = Event(
        type=EventTypes.COMMENTED.value,
        user_id=current_user.id,
        submission_id=submission_id,
    )
    comment.event = event
    db.session.add(event)
    db.session.add(comment)
    db.session.commit()
    return schema.dump(comment)
