from flask import Flask, render_template, request, redirect, url_for  
from sqlalchemy import create_engine  
from sqlalchemy.orm import sessionmaker  
from database_setup import Base, User, Anime, Complated, Plan_to_watch, Dropped
  
app = Flask(__name__)  
  
engine = create_engine('sqlite:///test.db')  
Base.metadata.bind = engine  
  
DBSession = sessionmaker(bind=engine)  
session = DBSession() 

def create_user(username, email):
    u = User(f"{username}", f"{email}")
    session.add(u)
    session.commit()

def delete_user(Id):
    a = session.query(User).filter_by(id=Id).one() 
    session.delete(a) 
    session.commit()

def add(table, userId, animeId):
    a = table(userId, animeId)
    session.add(a)
    session.commit()

def delete(table, uI):
    a = session.query(table).filter_by(userId=uI).one() 
    session.delete(a) 
    session.commit()

def read_anime():
    session.query(Anime).all()

@app.route("/")
def index():
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)