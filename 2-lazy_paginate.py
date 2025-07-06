import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def paginate_users(page_size, offset):
    """
    Fetches a page of users starting from a given offset.
    """
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", ""),
            database="ALX_prodev"
        )
        cursor = conn.cursor(dictionary=True)

        query = "SELECT * FROM user_data LIMIT %s OFFSET %s"
        cursor.execute(query, (page_size, offset))
        rows = cursor.fetchall()
        return rows

    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")
        return []
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

def lazy_paginate(page_size):
    """
    Generator that lazily loads one page of data at a time using LIMIT and OFFSET.
    """
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size




if __name__ == "__main__":
    for page in lazy_paginate(page_size=2):
        print("📦 New Page:")
        for user in page:
            print(user)
