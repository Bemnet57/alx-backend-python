import sqlite3

# Connect (or create if doesn't exist)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
)
''')

# Insert test data
cursor.executemany('INSERT INTO users (name, email) VALUES (?, ?)', [
    ('Alice', 'alice@example.com'),
    ('Bob', 'bob@example.com'),
    ('Charlie', 'charlie@example.com'),
])

# Commit and close
conn.commit()
conn.close()

print(" SQLite database and users table created successfully.")
