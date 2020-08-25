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
    # Update data on Friends table
    with connection.cursor() as cursor:
        cursor.execute("UPDATE Friends SET  age = 23 WHERE name = 'Bob';")
        connection.commit()
finally:
    # Close the connection, regardless of wheter the above was successful
    connection.close()