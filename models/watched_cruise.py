from models import db
from datetime import datetime

class WatchedCruise(db.Model):
    __tablename__ = 'watched_cruises'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Relates to User
    cruise_name = db.Column(db.String(255), nullable=False)  # Name of the cruise
    current_price = db.Column(db.Numeric, nullable=True)  # Latest known price
    tracking_started_at = db.Column(db.DateTime, default=datetime.utcnow)  # When tracking started

    # Relationship to User
    user = db.relationship('User', backref='watched_cruises', lazy=True)