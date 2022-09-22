from flask import Flask, render_template, g
import sqlite3

app = Flask(__name__)

MENUDB = 'music.db'



@app.route('/')
def index():
    db = sqlite3.connect(MENUDB)
    print(db)

    music = []
    cur = db.execute('SELECT * FROM top50')
    for row in cur:
        music.append(list(row))
    db.close()

    return render_template('index.html', 
        disclaimer='This website is for folks living in Aotearoa, New Zealand | Designed and Coded by Maggie McMillan-Perry',
        music=music)