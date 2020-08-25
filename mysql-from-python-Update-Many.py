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
    # Update Many data on Friends table 
    with connection.cursor() as cursor:
        rows = [(23,'Bob'),
        (24, 'Jim'),
        (25,'Fred')]
        cursor.executemany("UPDATE Friends SET  age = %s WHERE name = %s;",rows)
        connection.commit()
finally:
    # Close the connection, regardless of wheter the above was successful
    connection.close()