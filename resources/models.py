from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

db = SQLAlchemy()

class People(db.Model):
   __tablename__ = 'people'

   id = db.Column(db.Integer, primary_key = True)
   name = db.Column(db.String(120), nullable = False, unique = True)
   is_alive = db.Column(db.Integer, nullable = False, default = 1)
   is_king = db.Column(db.Integer, nullable = False, default = 0)
   place_id = db.Column(db.Integer, nullable = False)
