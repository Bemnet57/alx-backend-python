import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def stream_user_ages():
    """
    Generator that yields user ages one by one from the database.
    """
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", ""),
            database="ALX_prodev"
        )
        cursor = conn.cursor()

        cursor.execute("SELECT age FROM user_data")
        for (age,) in cursor:  # cursor returns tuple per row
            yield float(age)

    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()

def calculate_average_age():
    """
    Uses the stream_user_ages generator to compute the average age.
    """
    total = 0
    count = 0

    for age in stream_user_ages():
        total += age
        count += 1

    average = total / count if count else 0
    print(f"Average age of users: {average:.2f}")




if __name__ == "__main__":
    calculate_average_age()
