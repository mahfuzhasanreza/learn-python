import sqlite3

# Connect to database (creates it if not exists)
conn = sqlite3.connect("students.db")

# Create cursor
cur = conn.cursor()

print("Connected to database!")
conn.close()
