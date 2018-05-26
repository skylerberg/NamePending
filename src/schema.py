from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Email(allow_none=False)
    name = fields.Str(allow_none=False)
    is_admin = fields.Bool(dump_only=True)


class ChallengeSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(allow_none=False)
    description = fields.Str(allow_none=False)


class CommentSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int()
    user = fields.Nested(UserSchema, dump_only=True)
    content = fields.Str(allow_none=False)


class SubmissionSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(allow_none=False)
    user_id = fields.Int(dump_only=True)
    user = fields.Nested(UserSchema, dump_only=True)
    submission_id = fields.Int()
    content = fields.Str(allow_none=False)
    points = fields.Int(dump_only=True)
    comments = fields.Nested(CommentSchema, dump_only=True, many=True)


class EventSchema(Schema):
    id = fields.Int(dump_only=True)
    submission_id = fields.Int(dump_only=True)
    user_id = fields.Int(dump_only=True)
    submission_id = fields.Int(dump_only=True)
    time = fields.DateTime(dump_only=True, allow_none=False)
    type = fields.Str(allow_none=False)
    comment = fields.Nested(CommentSchema, allow_none=True)
