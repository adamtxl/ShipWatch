from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Initialize the SQLAlchemy instance

# Import models here AFTER initializing db
from .saved_search import SavedSearch
from .user import User
from .notification import Notification
from .price import Price
from .watched_cruise import WatchedCruise
from .destinations import Destination