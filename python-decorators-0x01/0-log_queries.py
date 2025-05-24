#!/usr/bin/python3

"""
A decorator that logs database queries
executed by any function
"""

import sqlite3
import functools
import logging

#### decorator to lof SQL queries

def log_queries(func):
    """ decorator function """

    logging.basicConfig(filename='{}.log'.format(func.__name__), level=logging.INFO)
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info('{}'.format(kwargs.get('query')))
        return func(*args, **kwargs)
    return wrapper



@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM user_data;")


