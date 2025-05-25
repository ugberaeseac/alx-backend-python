#!/usr/bin/python3

"""
decorator that manages database transactions
automatically commit or rollback changes
"""


import sqlite3 
import functools



def transactional(func):
    """ decorator function """
    @functools.wraps(func)
    def wrapper(connection, *args, **kwargs):
        try:
            cursor = connection.cursor()
            cursor.execute('BEGIN')
            result = func(connection, *args, **kwargs)
            connection.commit()
            return result
        except Exception as e:
            connection.rollback()
            raise e
        finally:
            connection.close()

    return wrapper



def with_db_connection(func):
    """ decorator function"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        connection = sqlite3.connect('users.db')
        try:
            result = func(connection, *args, **kwargs)
        finally:
            connection.close()
        return result
    return wrapper



@with_db_connection 
@transactional 
def update_user_email(conn, user_id, new_email): 
    cursor = conn.cursor() 
    cursor.execute("UPDATE user_data SET email = ? WHERE user_id = ?", (new_email, user_id)) 
#### Update user's email with automatic transaction handling 

update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')
