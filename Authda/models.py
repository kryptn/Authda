from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Invite(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String)
    referrer = db.Column(db.String)

    def __init__(self, email, referrer):
        self.email = email
        self.referrer = referrer

