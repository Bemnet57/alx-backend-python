import time
import sqlite3
import functools

# ✅ Query cache dictionary
query_cache = {}

# ✅ DB connection decorator from Task 2
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper

# ✅ Cache query results based on the SQL query string
def cache_query(func):
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        # Find the query string (positional or keyword)
        query = kwargs.get('query') if 'query' in kwargs else args[0] if args else None

        if query in query_cache:
            print(f"⚡ Using cached result for query: {query}")
            return query_cache[query]

        print(f"🔍 Executing and caching query: {query}")
        result = func(conn, *args, **kwargs)
        query_cache[query] = result
        return result
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# ✅ First call will execute and cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")
print(users)

# ✅ Second call will use cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")
print(users_again)
