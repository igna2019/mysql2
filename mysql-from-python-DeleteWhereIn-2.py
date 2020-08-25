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
    # Delete multiple rows based on a list of names
    with connection.cursor() as cursor:
        names = ['jim', 'Bob']
        cursor.execute("DELETE from  Friends  WHERE name in (%s,%s);", names)
        connection.commit()
finally:
    # Close the connection, regardless of wheter the above was successful
    connection.close()