#!/usr/bin/env python3
import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server (adjust user and password as needed)
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""  # Add your MySQL password if needed
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error: Could not connect or create database. {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        # Optional: print("MySQL connection closed.")
