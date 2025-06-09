from flask import Blueprint, request, jsonify
from models.meetup import Meetup, db
from models.meetup_participant import MeetupParticipant
from datetime import datetime

meetup_bp = Blueprint('meetup', __name__)

@meetup_bp.route('/create_meetup', methods=['POST'])
def create_meetup():
    data = request.get_json()
    new_meetup = Meetup(
        title=data['title'],
        location=data['location'],
        datetime=datetime.strptime(data['datetime'], '%Y-%m-%d %H:%M:%S'),
        created_by=data['created_by']
    )
    db.session.add(new_meetup)
    db.session.commit()
    
    return jsonify({"message": "Meetup created successfully!"}), 201

@meetup_bp.route('/join_meetup', methods=['POST'])
def join_meetup():
    data = request.get_json()
    new_participant = MeetupParticipant(
        user_id=data['user_id'],
        meetup_id=data['meetup_id'],
        transport_mode=data['transport_mode'],
        join_time=datetime.now()
    )
    db.session.add(new_participant)
    db.session.commit()
    
    return jsonify({"message": "Joined meetup successfully!"}), 201
