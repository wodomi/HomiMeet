from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class MeetupParticipant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    meetup_id = db.Column(db.Integer, db.ForeignKey('meetup.id'), nullable=False)
    transport_mode = db.Column(db.String(50), nullable=False)
    join_time = db.Column(db.DateTime, nullable=False)
    arrival_time = db.Column(db.DateTime, nullable=True)
