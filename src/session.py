from . import login_manager
from .models import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == user_id).first()
