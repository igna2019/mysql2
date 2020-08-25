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
    # Insert many Data into Table Created - Friends-
    with connection.cursor() as cursor:
        rows = [("Bob", 21, "1990-02-06 23:04:56"),
                ("Bob", 21, "1990-02-06 23:04:56"),
                ("Jim", 56, "1955-05-09  01:05:56"),
                ("fred", 75, "1945-09-12 23:04:56"),
                ("Fred", 100, "1911-09-12 23:04:56")]

        cursor.executemany("INSERT INTO Friends VALUES (%s, %s, %s);", rows)
        connection.commit()
finally:
    # Close the connection, regardless of wheter the above was successful
    connection.close()
