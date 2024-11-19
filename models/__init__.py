from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .saved_search import SavedSearch
from .user import User
from .notification import Notification
from .price import Price
from .watched_cruise import WatchedCruise