import sqlite3
import functools
from datetime import datetime  # ✅ Checker expects this

def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get('query') if 'query' in kwargs else args[0] if args else None
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] Executing SQL Query: {query}")
        return func(*args, **kwargs)
    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# Test run
if __name__ == "__main__":
    users = fetch_all_users(query="SELECT * FROM users")
    print(users)



# import sqlite3
# import functools

# def log_queries(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         # Extract the query string (assumes it's the first positional or named argument)
#         query = kwargs.get('query') if 'query' in kwargs else args[0] if args else None
#         print(f"📜 Executing SQL Query: {query}")
#         return func(*args, **kwargs)
#     return wrapper

# @log_queries
# def fetch_all_users(query):
#     conn = sqlite3.connect('users.db')
#     cursor = conn.cursor()
#     cursor.execute(query)
#     results = cursor.fetchall()
#     conn.close()
#     return results

# # Fetch users while logging the query
# users = fetch_all_users(query="SELECT * FROM users")
# print(users)
