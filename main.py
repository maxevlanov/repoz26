import sqlite3


conn = sqlite3.connect("db.db")
cur = conn.cursor()


cur.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    age INTEGER
); 
""")