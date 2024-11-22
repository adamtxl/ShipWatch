from models import db  # Import the shared db instance

class SavedSearch(db.Model):
    __tablename__ = 'saved_searches'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    destination_id = db.Column(db.Integer, db.ForeignKey('destinations.id'), nullable=False)  # Foreign Key
    price_min = db.Column(db.Float, nullable=True)
    price_max = db.Column(db.Float, nullable=True)
    number_of_nights = db.Column(db.Integer, nullable=True)  # New Column
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)

    # Relationships
    user = db.relationship('User', backref='saved_searches')
    destination = db.relationship('Destination', backref='saved_searches')  # New Relationship