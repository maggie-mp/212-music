from flask import Flask, render_template, g
import sqlite3

app = Flask(__name__)

MENUDB = 'music.db'

@app.route('/')
def index():
    db = sqlite3.connect(MENUDB)
    print(db)

    music = []
    cur = db.execute('SELECT * FROM music')
    for row in cur:
        music.append(list(row))
    db.close()

    return render_template('index.html',
            )
