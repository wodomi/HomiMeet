from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Meetup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    location = db.Column(db.Text, nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    status = db.Column(db.Enum('scheduled', 'canceled', 'done'), default='scheduled')
