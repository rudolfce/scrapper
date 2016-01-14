from sqlalchemy import Column, Integer, String
from .__init__ import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    username = Column(String(30), unique=True)
    bio = Column(String)
    location = Column(String(50))
    query_date = Column(String(20))

    def __init__(self, name, username, bio, location, query_date):
        self.name = name
        self.username = username
        self.bio = bio
        self.location = location
        self.query_date = query_date

    def __repr__(self):
        return "<User {0!r}>".format(self.username)

    def get_dict(self):
        return {"name": self.name,
                "username": self.username,
                "bio": self.bio,
                "location": self.location,
                "query_date": self.query_date}
