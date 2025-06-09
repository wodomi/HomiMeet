from flask import Blueprint

auth_bp = Blueprint('auth', __name__)
meetup_bp = Blueprint('meetup', __name__)
user_bp = Blueprint('user', __name__)

from . import auth, meetup, user
