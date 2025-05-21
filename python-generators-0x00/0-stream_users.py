#!/usr/bin/python3

"""
Generator function that streams rows from
an SQL database one by one
"""

import mysql.connector
from mysql.connector import errorcode


def stream_users():
    """ stream rows from SQL database"""
    db_config = {
                'host': 'localhost',
                'user': 'admin',
                'password': 'Testing101#',
                'database': 'ALX_prodev'
        }

    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
    except mysql.connector.Error as err:
            print(err)
    else:
        cursor.execute("SELECT * FROM user_data;")
        while True:
            row = cursor.fetchone()
            if row is None:
                break
            yield row
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


stream_users()
