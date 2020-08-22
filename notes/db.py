from app import db
from app import ma

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(32))

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User {email}>'.format(email=self.email)


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    text = db.Column(db.Text())
    user_id = db.Column(db.Integer)

    def __init__(self, title, text, user_id):
        self.title = title
        self.text = text
        self.user_id = user_id

    def __repr__(self):
        return '<Note {title}>'.format(title=self.title)