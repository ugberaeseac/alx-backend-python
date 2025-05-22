#!/usr/bin/python3
"""
lazy loading paginated data
generator function to lazily load each page
from users database
- use only one loop
- use the yield generator
"""

seed = __import__('seed')



def paginate_users(page_size, offset):
    """
    fetch the next page when loaded using offset
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows



def lazy_paginate(page_size):
    """fetch data from users database using generator
    to load each page
    """
    offset = 0
    while True:
        rows = paginate_users(page_size, offset)
        if rows is None:
            break
        yield rows
        offset += page_size

