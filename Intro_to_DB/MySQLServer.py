#!/usr/bin/python3
"""
Script that creates the database hbtn_0c_0 in your MySQL server.
"""

import mysql.connector

try:
    # Establish the connection to the MySQL server
    # NOTE: Use the credentials for your ALX sandbox environment
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root"
    )

    # Create a cursor object
    cursor = db.cursor()

    # SQL command to create the database if it does not exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the cursor and connection
    if 'cursor' in locals() and cursor is not None:
        cursor.close()
    if 'db' in locals() and db.is_connected():
        db.close()
