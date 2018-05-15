from marshmallow import Schema, fields


class ChallengeSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(allow_none=False)
    description = fields.Str(allow_none=False)


class SubmissionSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(allow_none=False)
    user_id = fields.Int()
    submission_id = fields.Int()
    content = fields.Str(allow_none=False)
    score = fields.Int(dump_only=True)


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Email(allow_none=False)
    is_admin = fields.Bool(dump_only=True)


class CommentSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int()
    user = fields.Nested(UserSchema, dump_only=True)
    submission_id = fields.Int()
    content = fields.Str(allow_none=False)
