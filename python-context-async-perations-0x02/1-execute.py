import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Add age column if it doesn't exist
cursor.execute("ALTER TABLE users ADD COLUMN age INTEGER")

# Set age for existing users
cursor.execute("UPDATE users SET age = 28 WHERE name = 'Alice'")
cursor.execute("UPDATE users SET age = 34 WHERE name = 'Bob'")
cursor.execute("UPDATE users SET age = 22 WHERE name = 'Charlie'")

conn.commit()
conn.close()

print("✅ Age column added and populated.")

class ExecuteQuery:
    def __init__(self, db_name, query, params=()):
        self.db_name = db_name
        self.query = query
        self.params = params
        self.connection = None
        self.results = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        cursor = self.connection.cursor()
        cursor.execute(self.query, self.params)
        self.results = cursor.fetchall()
        return self.results  # returned to the `as result` part

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()
            print("✅ Connection closed.")

# ✅ Usage example
query = "SELECT * FROM users WHERE age > ?"
param = (25,)

with ExecuteQuery('users.db', query, param) as result:
    print("📋 Users older than 25:")
    for row in result:
        print(row)


# #added later
# import sqlite3

# conn = sqlite3.connect('users.db')
# cursor = conn.cursor()

# # Add age column if it doesn't exist
# cursor.execute("ALTER TABLE users ADD COLUMN age INTEGER")

# # Set age for existing users
# cursor.execute("UPDATE users SET age = 28 WHERE name = 'Alice'")
# cursor.execute("UPDATE users SET age = 34 WHERE name = 'Bob'")
# cursor.execute("UPDATE users SET age = 22 WHERE name = 'Charlie'")

# conn.commit()
# conn.close()

# print("✅ Age column added and populated.")
