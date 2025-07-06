import csv
import uuid
import mysql.connector
from mysql.connector import errorcode
import os
from dotenv import load_dotenv

load_dotenv()

def connect_db():
    """Connect to MySQL server (without specifying a database)."""
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "")
    )

def create_database(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        print("✅ Database created or already exists.")
    except mysql.connector.Error as err:
        print(f"❌ Failed creating database: {err}")
    cursor.close()

def connect_to_prodev():
    """Connect directly to ALX_prodev database."""
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database="ALX_prodev"
    )

def create_table(connection):
    cursor = connection.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS user_data (
        user_id CHAR(36) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        age DECIMAL NOT NULL,
        INDEX(email)
    )
    """
    cursor.execute(query)
    connection.commit()
    print("✅ Table created or already exists.")
    cursor.close()

def insert_data(connection, data):
    cursor = connection.cursor()
    insert_query = """
    INSERT IGNORE INTO user_data (user_id, name, email, age)
    VALUES (%s, %s, %s, %s)
    """
    for row in data:
        cursor.execute(insert_query, (
            str(uuid.uuid4()), row["name"], row["email"], row["age"]
        ))
    connection.commit()
    print("✅ Data inserted.")
    cursor.close()

def load_csv_data(filepath):
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

if __name__ == "__main__":
    try:
        # Connect & setup
        conn = connect_db()
        create_database(conn)
        conn.close()

        # Table & data
        conn = connect_to_prodev()
        create_table(conn)
        user_data = load_csv_data("user_data.csv")
        insert_data(conn, user_data)
        conn.close()
    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")
