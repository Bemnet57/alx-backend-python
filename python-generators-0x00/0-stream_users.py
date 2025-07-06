import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def stream_users():
    """
    Generator that streams rows one-by-one from user_data table.
    """
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", ""),
            database="ALX_prodev"
        )
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM user_data")
        for row in cursor:
            yield row  # Yield each row as a dictionary

    except mysql.connector.Error as err:
        print(f"❌ Database error: {err}")
    finally:
        cursor.close()
        conn.close()





if __name__ == "__main__":
    for user in stream_users():
        print(user)
