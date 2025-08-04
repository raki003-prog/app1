import pandas as pd
import sqlite3
import os

# File paths
file1_path = os.path.join("data", "orders.csv")
file2_path = os.path.join("data", "users.csv")

# Read CSVs
df1 = pd.read_csv(file1_path)
df2 = pd.read_csv(file2_path)

# Create DB connection (this will create 'database.db' if it doesn't exist)
conn = sqlite3.connect("database.db")

# Write to SQLite tables
df1.to_sql("table1", conn, if_exists="replace", index=False)
df2.to_sql("table2", conn, if_exists="replace", index=False)

# Confirm tables
print("Tables created:")
print(conn.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall())

conn.close()
