import sqlite3

def get_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row  # So rows behave like dictionaries
    return conn
