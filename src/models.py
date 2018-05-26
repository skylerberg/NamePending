from datetime import datetime

from sqlalchemy.orm import backref
from flask_login import UserMixin

from . import db
from .enums import EventTypes, SubmissionStatus


class Challenge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)

    event = db.relationship('Event', backref=backref('comment', uselist=False), foreign_keys=[event_id])


class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    challenge_id = db.Column(db.Integer, db.ForeignKey('challenge.id'), nullable=False)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    score = db.Column(db.Integer, nullable=True)
    _status = db.Column('status', db.Text, nullable=False)
    points = db.Column(db.Text, nullable=False, default=0)

    user = db.relationship('User', backref='submissions', foreign_keys=[user_id])
    challenge = db.relationship('Challenge', backref='submissions', foreign_keys=[challenge_id])

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        SubmissionStatus(value)  # Throw if value is not valid for this enum
        self._status = value

    @property
    def comments(self):
        comments = []
        for event in self.events:
            if event.comment:
                comments.append(event.comment)
        return comments


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text, nullable=False, unique=True)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)


class Event(db.Model):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.time = datetime.now()

    id = db.Column(db.Integer, primary_key=True)
    submission_id = db.Column(db.Integer, db.ForeignKey('submission.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    _type = db.COlumn('type', db.Text, nullable=False)

    user = db.relationship('User', foreign_keys=[user_id])
    submission = db.relationship('Submission', foreign_keys=[submission_id], backref='events')

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        EventTypes(value)  # Throw if value is not valid for this enum
        self._type = value
