from flask_login import UserMixin

from . import db


class Challenge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    submission_id = db.Column(db.Integer, db.ForeignKey('submission.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, nullable=False)

    submission = db.relationship('Submission', backref='comments', foreign_keys=[submission_id])
    user = db.relationship('User', backref='comments', foreign_keys=[user_id])


class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    challenge_id = db.Column(db.Integer, db.ForeignKey('challenge.id'), nullable=False)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    score = db.Column(db.Integer, nullable=True)
    created = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Text, nullable=False)

    user = db.relationship('User', backref='submissions', foreign_keys=[user_id])
    challenge = db.relationship('Challenge', backref='submissions', foreign_keys=[challenge_id])


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text, nullable=False, unique=True)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)


class Points(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)
    submission_id = db.Column(db.Integer, db.ForeignKey('submission.id'), nullable=False)
    granted_by_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created = db.Column(db.DateTime, nullable=False)

    granted_by = db.relationship('User', foreign_keys=[granted_by_id])
