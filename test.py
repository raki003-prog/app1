import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()
cursor.execute("PRAGMA table_info(table1);")
columns = cursor.fetchall()
conn.close()

for col in columns:
    print(col)
