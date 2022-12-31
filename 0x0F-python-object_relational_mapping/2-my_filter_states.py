#!/usr/bin/python3
"""
This is a script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa
where name matches the argument."""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """
    db_connect = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    db_cursor = db_connect.cursor()

    db_cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' \
            ORDER BY id".format(argv[4]))

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
