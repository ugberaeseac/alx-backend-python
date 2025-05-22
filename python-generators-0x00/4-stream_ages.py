#!/usr/bin/python3
"""
Generator function to compute the
average age for a large dataset
"""

seed = __import__('seed')


def stream_user_ages():
    """ yields ages one by one    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT age from user_data;")
    for row in cursor:
        yield row['age']
    connection.close()

def average_age():
    """ calculate the average age """
    sum_age = 0
    count_age = 0
    for age in stream_user_ages():
        sum_age += age
        count_age += 1
    
    avg_age = sum_age // count_age
    print(f'Average age of users: {avg_age}')


average_age()

