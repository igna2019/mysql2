import os
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
    # Run a query- each row will be presented as dictionaries
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = 'SELECT * FROM Genre;'
        cursor.execute(sql)
        for row in cursor:
            print(row)
finally:
    # Close the connection, regardless of wheter the above was successful
    connection.close()
