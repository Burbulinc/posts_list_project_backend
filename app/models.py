from app import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    likes = db.Column(db.Integer)
    user_name = db.Column(db.String(64))
    type = db.Column(db.String(20))
    text = db.Column(db.String(128))
