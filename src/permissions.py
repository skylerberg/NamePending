from collections import namedtuple
from functools import partial

from flask_login import current_user
from flask_principal import identity_loaded, Permission

from . import app

BaseNeed = namedtuple('BasePermission', ['need_name', 'identifier'])

SubmissionOwnerNeed = partial(BaseNeed, 'submission_owner')


class SubmissionOwnerPermission(Permission):
    def __init__(self, submission_id):
        need = SubmissionOwnerNeed(submission_id)
        super().__init__(need)


@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    identity.user = current_user

    if hasattr(current_user, 'submissions'):
        for submission in current_user.submissions:
            identity.provides.add(SubmissionOwnerPermission(submission.id))
