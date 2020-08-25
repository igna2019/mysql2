import os
import datetime
import pymysql
# Get username from Cloud9 workspace
# (Modify this variable if running on another environment)
username = os.getenv('C9_USER')

# connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    # Alternate Delete using String Interpolation  a row  data on Friends table
    with connection.cursor() as cursor:
        rows = cursor.executemany("DELETE from  Friends  WHERE name = %s;", ['Bob', 'Jim'])
        connection.commit()
finally:
    # Close the connection, regardless of wheter the above was successful
    connection.close()