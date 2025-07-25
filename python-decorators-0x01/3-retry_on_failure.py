import time
import sqlite3
import functools

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

# ✅ Retry decorator with configurable retries & delay
def retry_on_failure(retries=3, delay=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"⚠️ Attempt {attempt} failed: {e}")
                    if attempt == retries:
                        print("❌ Max retries reached. Giving up.")
                        raise
                    print(f"⏳ Retrying in {delay} second(s)...")
                    time.sleep(delay)
        return wrapper
    return decorator

@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

# ✅ Attempt to fetch users with retry logic
users = fetch_users_with_retry()
print(users)
