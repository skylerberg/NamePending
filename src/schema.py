from marshmallow import Schema, fields
from marshmallow_enum import EnumField


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Email(allow_none=False)
    name = fields.Str(allow_none=False)
    is_admin = fields.Bool(dump_only=True)


class ChallengeSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(allow_none=False)
    description = fields.Str(allow_none=False)


class SubmissionSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(allow_none=False)
    user_id = fields.Int(dump_only=True)
    user = fields.Nested(UserSchema, dump_only=True)
    submission_id = fields.Int()
    content = fields.Str(allow_none=False)
    score = fields.Int(dump_only=True)
    created = fields.DateTime(dump_only=True, allow_none=False)
    status = fields.Str(dump_only=True)


class CommentSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int()
    user = fields.Nested(UserSchema, dump_only=True)
    submission_id = fields.Int()
    content = fields.Str(allow_none=False)
    created = fields.DateTime(dump_only=True, allow_none=False)


class PointsSchema(Schema):
    id = fields.Int(dump_only=True)
    granted_by_id = fields.Int(dump_only=True)
    granted_by = fields.Nested(UserSchema, dump_only=True)
    submission_id = fields.Int(dump_only=True)
    amount = fields.Int(allow_none=False)
    created = fields.DateTime(dump_only=True, allow_none=False)
