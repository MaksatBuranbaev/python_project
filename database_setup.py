import sys  

from sqlalchemy import Column, ForeignKey, Integer, String  
  
from sqlalchemy.ext.declarative import declarative_base  
  
from sqlalchemy.orm import relationship  
  
from sqlalchemy import create_engine  
  
Base = declarative_base()  
  
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True)
    email = Column(String(120), unique=True)
    anime_completed = relationship('Complated', backref='user', lazy=True)
    anime_plan_to_watch = relationship('Plan_to_watch', backref='user', lazy=True)
    anime_dropped = relationship('Dropped', backref='user', lazy=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

class Complated(Base):
    __tablename__ = 'complated'

    id = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey('user.id'))
    animeId = Column(Integer, ForeignKey('anime.id'))

    def __init__(self, userId, animeId):
        self.userId = userId
        self.animeId = animeId

class Plan_to_watch(Base):
    __tablename__ = 'plan_to_watch'

    id = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey('user.id'))
    animeId = Column(Integer, ForeignKey('anime.id'))

    def __init__(self, userId, animeId):
        self.userId = userId
        self.animeId = animeId

class Dropped(Base):
    __tablename__ = 'dropped'

    id = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey('user.id'))
    animeId = Column(Integer, ForeignKey('anime.id'))

    def __init__(self, userId, animeId):
        self.userId = userId
        self.animeId = animeId

class Anime(Base):
    __tablename__ = 'anime'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True)
    description = Column(String(360), unique=True)
    anime_completed = relationship('Complated', backref='anime', lazy=True)
    anime_plan_to_watch = relationship('Plan_to_watch', backref='anime', lazy=True)
    anime_dropped = relationship('Dropped', backref='anime', lazy=True)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return '<Anime %r>' % self.name

engine = create_engine('sqlite:///test.db')  
  
Base.metadata.create_all(engine)