
# database.py - SQLite Database

import sqlite3

def init_db():
    conn = sqlite3.connect('watchlist.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS watchlist
                 (username TEXT, title TEXT, release_date TEXT, rating REAL, overview TEXT)''')
    conn.commit()
    conn.close()

def add_movie(username, movie):
    conn = sqlite3.connect('watchlist.db')
    c = conn.cursor()
    c.execute('INSERT INTO watchlist VALUES (?, ?, ?, ?, ?)', 
              (username, movie['title'], movie['release_date'], movie['rating'], movie['overview']))
    conn.commit()
    conn.close()

def get_watchlist(username):
    conn = sqlite3.connect('watchlist.db')
    c = conn.cursor()
    c.execute('SELECT title, release_date, rating, overview FROM watchlist WHERE username = ?', (username,))
    movies = c.fetchall()
    conn.close()
    return movies

def delete_watchlist(username):
    conn = sqlite3.connect('watchlist.db')
    c = conn.cursor()
    c.execute('DELETE FROM watchlist WHERE username = ?', (username,))
    conn.commit()
    conn.close()
