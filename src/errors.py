from sqlalchemy.exc import IntegrityError
from marshmallow.exceptions import ValidationError
from flask_json import json_response

from . import app


@app.errorhandler(IntegrityError)
def integrity(exception):
    return json_response(
        status_=400,
        error='Bad data')


@app.errorhandler(ValidationError)
def validation(exception):
    return json_response(
        status_=400,
        error='Validation failed')
