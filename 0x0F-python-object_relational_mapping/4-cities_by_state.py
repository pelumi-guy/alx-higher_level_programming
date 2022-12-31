#!/usr/bin/python3
"""
This is a script that lists all cities from the database hbtn_0e_4_usa
"""

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

    db_cursor.execute("SELECT c.id, c.name, s.name\
            FROM cities AS c\
            CROSS JOIN states AS s\
            ON c.state_id = s.id\
            ORDER BY c.id")

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
