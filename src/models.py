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

    submission = db.relationship('Submission', backref='comments', foreign_keys=[submission_id])
    user = db.relationship('User', backref='comments', foreign_keys=[user_id])


class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    score = db.Column(db.Integer, nullable=True)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
