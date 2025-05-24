#!/usr/bin/python3

"""
decorator that opens a database
passes it to a function and closes
the connection
"""

import sqlite3 
import functools

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
def get_user_by_id(conn, user_id):
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM user_data WHERE user_id = ?", (user_id,)) 
    return cursor.fetchone() 
#### Fetch user by ID with automatic connection handling 

user = get_user_by_id(user_id=1)
print(user)
