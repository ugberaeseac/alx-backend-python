#!/usr/bin/python3

"""
Python script that sets up the MySQL database
creates a connection to the MySQL server,
creates database and table and populate with sample data from a csv file.
"""

import mysql.connector
import csv


def connect_db():
    """connects to the MySQL server"""
    config = {
                'host':'localhost',
                'user': 'admin',
                'password': 'Testing101#'
            }
    connection = mysql.connector.connect(**config)
    if connection:
        return connection


def create_database(connection):
    """ creates the database ALX_prodev """
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev;")
        finally:
            cursor.close()


def connect_to_prodev():
    """ connects to the database"""
    config = {
                'host':'localhost',
                'user':'admin',
                'password': 'Testing101#',
                'database': 'ALX_prodev'
            }
    connection = mysql.connector.connect(**config)
    if connection:
        return connection


def create_table(connection):
    """ creates user_data table"""
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("""	CREATE TABLE IF NOT EXISTS user_data (
				user_id VARCHAR(36) PRIMARY KEY,
				name VARCHAR(255) NOT NULL,
			    email VARCHAR(255) NOT NULL,
				age INTEGER NOT NULL,
				INDEX (user_id))
            """
            )
            print('Table user_data created successfully')
        finally:
            cursor.close()


def insert_data(connection, data):
    """ populate database with sample data from csvfile """
    import uuid

    cursor = connection.cursor()
    with open(data, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for line in csv_reader:
            cursor.execute("INSERT INTO user_data VALUES(%s, %s, %s, %s)",
            (str(uuid.uuid4()), line['name'], line['email'], line['age']))

    connection.commit()
    cursor.close()
