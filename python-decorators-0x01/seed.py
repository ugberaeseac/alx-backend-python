#!/usr/bin/python3

"""
Python script that sets up the MySQL database
creates a connection to the MySQL server,
creates database and table and populate with sample data from a csv file.
"""

import sqlite3
import csv


def connect_db():
    """connects to the MySQL server"""
    connection = sqlite3.connect('users.db')
    if connection:
        return connection



def create_table(connection):
    """ creates user_data table"""
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("""	CREATE TABLE IF NOT EXISTS user_data (
				user_id INTEGER PRIMARY KEY,
				name TEXT,
			    email TEXT,
				age INTEGER)
            """
            )
            print('Table user_data created successfully')
        finally:
            cursor.close()
            connection.commit()


def insert_data(connection, data):
    """ populate database with sample data from csvfile """

    cursor = connection.cursor()
    with open(data, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        count = 0
        for line in csv_reader:
            count += 1
            cursor.execute("INSERT INTO user_data VALUES(?, ?, ?, ?)",
            (count, line['name'], line['email'], line['age']))

    connection.commit()
    cursor.close()


connection = connect_db()
#create_table(connection)
#insert_data(connection, 'user_data.csv')

cursor = connection.cursor()
cursor.execute('SELECT * FROM user_data;')
for rows in cursor:
    print(rows)
