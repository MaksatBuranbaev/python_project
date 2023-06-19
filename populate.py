from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import User, Anime, Complated, Plan_to_watch, Dropped, Base

engine = create_engine('sqlite:///test.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()