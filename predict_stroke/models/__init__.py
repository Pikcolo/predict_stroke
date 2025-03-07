import mongoengine as me
from flask_mongoengine import MongoEngine
from .users import User
from .stroke_model import load_stroke_model
from .scaler_model import load_scaler_model

__all__ = [
   "User",
   "load_stroke_model",
   "load_scaler_model"
]


db = MongoEngine()


def init_db(app):
   db.init_app(app)
