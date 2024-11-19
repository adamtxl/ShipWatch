from models import db
from datetime import datetime

class Price(db.Model):
    __tablename__ = 'prices'
    id = db.Column(db.Integer, primary_key=True)
    cruise_id = db.Column(db.Integer, db.ForeignKey('watched_cruises.id'), nullable=False)  # Relates to WatchedCruise
    price = db.Column(db.Numeric, nullable=False)  # Store price as a number
    captured_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp for when the price was captured

    # Relationship to WatchedCruise
    cruise = db.relationship('WatchedCruise', backref='prices', lazy=True)