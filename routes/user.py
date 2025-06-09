from flask import Blueprint, jsonify
from models.user import User

user_bp = Blueprint('user', __name__)

@user_bp.route('/profile/<int:user_id>', methods=['GET'])
def get_profile(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify({
            "username": user.username,
            "bio": user.bio,
            "avatar_url": user.avatar_url
        }), 200
    return jsonify({"message": "User not found!"}), 404
