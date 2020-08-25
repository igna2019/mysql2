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
    #Update data on Friends table with alternate 
    with connection.cursor() as cursor:
        cursor.execute("UPDATE Friends SET  age = %s WHERE name = %s;",
        (23, 'Bob'))
        connection.commit()
finally:
    # Close the connection, regardless of wheter the above was successful
    connection.close()
