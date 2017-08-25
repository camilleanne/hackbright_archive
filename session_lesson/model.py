import sqlite3

DB = None
CONN = None

ADMIN_USER="hackbright"
ADMIN_PASSWORD=5980025637247534551

def authenticate(username, password):
    connect_to_db()
    command = None
    password = hash(password)
    query = """SELECT id FROM users WHERE username = ? AND password = ?"""
    DB.execute(query, (username, password))
    row = DB.fetchone()
    if row:
        return row[0]
    else: 
        return None

def get_user_by_name(username):
    connect_to_db()
    command = None
    query = """SELECT id FROM users WHERE username = ?"""
    DB.execute(query, (username,))
    row = DB.fetchone()
    print row
    return row

def get_user_by_id(user_id):
    connect_to_db()
    command = None
    query = """SELECT username FROM users WHERE id = ?"""
    DB.execute(query, (user_id,))
    row = DB.fetchone()
    return row[0]

def return_wall_posts(user_id):
    connect_to_db()
    command = None
    query = """SELECT username, created_at, content FROM wall_posts INNER JOIN users 
                on wall_posts.author_id= users.id WHERE owner_id = ? """
    DB.execute(query, (user_id[0], ))
    rows = DB.fetchall()
    return rows

def add_wall_post_to_db(user_id, author_id, content):
    connect_to_db()
    command = None
    query = """INSERT INTO wall_posts (owner_id, author_id, created_at, content) VALUES (?,?,datetime('now'),?)"""
    DB.execute(query, (user_id[0], author_id, content))
    CONN.commit()


def add_user_to_db(username, password):
    connect_to_db()
    command = None
    query = """INSERT INTO users (username, password) VALUES (?, ?)"""
    DB.execute(query, (username, hash(password)))
    CONN.commit()

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("thewall.db")
    DB = CONN.cursor()