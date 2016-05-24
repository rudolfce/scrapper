from scrapper import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    username = db.Column(db.String(30), unique=True)
    bio = db.Column(db.String(160))
    location = db.Column(db.String(160))
    query_date = db.Column(db.String(20))
    exists = db.Column(db.Boolean)

    def __init__(self, name='', username='', bio='', location='', query_date='',
                 exists=False):
        self.name = name
        self.username = username
        self.bio = bio
        self.location = location
        self.query_date = query_date
        self.exists = exists

    def __repr__(self):
        return "<User {0!r}>".format(self.username)

    def save(self, commit=True):
        db.session.add(self)
        if commit:
            db.session.commit()

    def update(self, commit=True):
        db.session.refresh(self)
        if commit:
            db.session.commit()

    def get_dict(self):
        return {"name": self.name,
                "username": self.username,
                "bio": self.bio,
                "location": self.location,
                "query_date": self.query_date,
                "exists": self.exists}
