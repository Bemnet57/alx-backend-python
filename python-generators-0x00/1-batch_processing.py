import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def stream_users_in_batches(batch_size):
    """
    Generator that yields batches of users from the user_data table.
    Each batch contains up to `batch_size` rows.
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
        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break
            yield batch

    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")
    finally:
        cursor.close()
        conn.close()


# def batch_processing(batch_size):
#     """
#     Processes each batch of users, filtering users over age 25.
#     Yields only users with age > 25.
#     """
#     for batch in stream_users_in_batches(batch_size):
#         for user in batch:
#             if float(user["age"]) > 25:
#                 yield user

def batch_processing(batch_size):
    """
#     Processes each batch of users, filtering users over age 25.
#     Yields only users with age > 25.
#     """


    filtered = []
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if float(user["age"]) > 25:
                filtered.append(user)
    return filtered




if __name__ == "__main__":
    for user in batch_processing(batch_size=2):
        print(user)