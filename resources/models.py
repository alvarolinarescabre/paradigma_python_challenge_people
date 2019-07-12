from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Sequence

db = SQLAlchemy()

class People(db.Model):
   __tablename__ = 'people'

   id = db.Column(db.Integer, primary_key = True)
   name = db.Column(db.String(120), nullable = False, unique = True)
   is_alive = db.Column(db.Integer, nullable = False, default = 1)
   place_id = db.Column(db.Integer, nullable = False)
