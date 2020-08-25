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
    # Create a Table
    with connection.cursor() as cursor:
        cursor.execute("""CREATE TABLE IF NOT EXISTS
                        Friends(name char(20), age int, DOB datetime);""")
        # Note that the above will still display a warning (not error) table 
        #already exists
finally:
    # Close the connection, regardless of wheter the above was successful
    connection.close()
