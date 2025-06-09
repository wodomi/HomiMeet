from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    meetup_id = db.Column(db.Integer, db.ForeignKey('meetup.id'), nullable=False)
    punctuality = db.Column(db.Enum('early', 'on_time', 'late', 'missed'), nullable=False)
    score_change = db.Column(db.Integer, nullable=False)
