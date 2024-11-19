from models import db
from datetime import datetime

class Notification(db.Model):
    __tablename__ = 'notifications'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Relates to User
    message = db.Column(db.Text, nullable=False)  # Notification content
    sent_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp for when it was sent

    # Relationship to User
    user = db.relationship('User', backref='notifications', lazy=True)