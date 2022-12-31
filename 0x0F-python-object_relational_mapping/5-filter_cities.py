#!/usr/bin/python3
"""
This is a script that takes in the name of a state 
as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa"""

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

    db_cursor.execute("SELECT c.name\
            FROM cities AS c\
            CROSS JOIN states AS s\
            ON c.state_id = s.id\
            WHERE s.name LIKE BINARY '{}'\
            ORDER BY c.id".format(argv[4]))

    rows_selected = db_cursor.fetchall()

    for i, row in enumerate(rows_selected):
        print(row[0], end='')
        if i < len(rows_selected) - 1:
            print(', ', end='')
        else:
            print()
