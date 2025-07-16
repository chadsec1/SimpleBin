import sqlite3
import os

DB_PATH = "app/database.db"

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    if not os.path.exists(DB_PATH):
        conn = get_db()
        c = conn.cursor()
        c.execute('''
            CREATE TABLE pastes (
                id TEXT PRIMARY KEY,
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                ip TEXT,
                user_agent TEXT
            )
        ''')
        conn.commit()
        conn.close()
        print("[DB] Created new database.")
    else:
        print("[DB] Already exists.")
