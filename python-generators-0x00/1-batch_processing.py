#!/usr/bin/python3

"""
Generator function that fetches and processes
data in batches from the users database
- uses no more than 2 loops
- uses the yield generator
"""


import mysql.connector
from mysql.connector import errorcode

db_config = {
                'name': 'localhost',
                'user': 'admin',
                'password': 'Testing101@',
                'database': 'ALX_prodev';
        }


connection = mysql.connector.connect(**db_config)
cursor = connection.cursor(dictionary=True)


def stream_users_in_batches(batch_size):
    """fetches rows in batches """

    cursor.execute('SELECT * FROM user_data LIMIT %s;', (batch_size,))
    rows = cursor.fetchall()
    for row in rows:
        yield row



def batch_processing(batch_size):
    """processes each batch and filter by age """

    batch = stream_users_in_batches(batch_size)
    if batch:
        for row in batch:
            if (row['age']) > 25:
                print(row)



