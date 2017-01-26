from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Status:
    invited = 'invited'
    rejected = 'rejected'
    submitted = 'submitted'
    resubmitted = 'resubmitted'

    @property
    def enum(self):
        return (self.invited,
                self.rejected,
                self.submitted,
                self.resubmitted)


class Invite(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String)
    referrer = db.Column(db.String)
    status = db.Column(db.String(15), default=Status.submitted)
    notes = db.Column(db.Text)
    created = db.Column(db.DateTime, server_default=db.func.now())
    last_modified = db.Column(db.DateTime, onupdate=db.func.now())

    def __init__(self, email, referrer):
        self.email = email
        self.referrer = referrer

    def invite(self):
        self.status = Status.invited
        db.session.commit()

    def reject(self):
        self.status = Status.rejected
        db.session.commit()

    @staticmethod
    def get_pending():
        query = Invite.status.in_((Status.submitted, Status.resubmitted))
        return Invite.query.filter(query).all()

    @staticmethod
    def get_or_create(email, referrer):
        result = Invite.query.filter_by(email=email).first()

        if not result:
            result = Invite(email, referrer)
            db.session.add(result)
        else:
            result.status = Status.resubmitted

        db.session.commit()        
        return result

    def to_json(self):
        return {'id': self.id,
                'email': self.email,
                'referrer': self.referrer,
                'status': self.status,
                'notes': self.notes,
                'created': self.created,
                'last_modified': self.last_modified,}


