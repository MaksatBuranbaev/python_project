import sqlite3
from flask import Flask, redirect, url_for, render_template, request

login = True
app = Flask(__name__)

def command_db(name_db, command): #пример работы запросов в sqlite
    conn = sqlite3.connect(name_db)
    cur = conn.cursor()
    cur.execute(command)
    conn.commit()

def add_anime(user, category, anime_name):
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute(f"""INSERT INTO {user}({category}) 
   VALUES("{anime_name}");""")
    conn.commit()

def get_anime():
    conn = sqlite3.connect("anime.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM anime")
    return cur.fetchall()

def create_user(user, password):
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {user} 
        (
	"Completed"	TEXT,
	"Dropped"	TEXT,
	"Plan to Watch"	TEXT
);"""
        )
    flag = True
    cur.execute("SELECT * FROM users")
    for uuser in cur.fetchall():
        if uuser[1] == user:
            flag = False
    if flag:
        cur.execute(f"""INSERT INTO users(name, password) 
   VALUES("{user}", "{password}");""")
    conn.commit()

@app.route("/")
def index():
    if login == True:
        return render_template('index.html')
    else:
         return render_template('index.html')
        #return redirect(url_for('login'))
   
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/logout')
def logout():
    return redirect(url_for('index'))

@app.route('/anime')
def anime():
    anime = get_anime()
    #...
    return render_template('anime.html')

if __name__ == '__main__':
    app.run(debug=True)
# в templates есть только index.html, остальных нет т.к. я не знаю html код а просто копипастить смысла нет
