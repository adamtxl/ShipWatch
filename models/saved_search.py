from . import db  # Import the SQLAlchemy instance

class SavedSearch(db.Model):
    __tablename__ = 'saved_searches'  # Name of the database table

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier
    user_id = db.Column(db.Integer, nullable=False)  # Link to a specific user (future expansion)
    destination = db.Column(db.String(255), nullable=False)  # Destination to search for
    price_min = db.Column(db.Float, nullable=False)  # Minimum price
    price_max = db.Column(db.Float, nullable=False)  # Maximum price
    created_at = db.Column(db.DateTime, default=db.func.now())  # Timestamp for when the search was saved