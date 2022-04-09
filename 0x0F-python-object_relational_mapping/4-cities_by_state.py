#!/usr/bin/python3
"""Show states in database."""
import MySQLdb as sql
from sys import argv


def main(user, passw, db):
    """Show cities in database and print result in order."""
    db = sql.connect(host='localhost', user=user,
                     passwd=passw, db=db, port=3306)
    c = db.cursor()
    c.execute("""
            SELECT c.id, c.name, s.name
            FROM cities c
            INNER JOIN states s ON s.id = c.state_id
            ORDER BY id;
            """)
    res = c.fetchall()
    for r in res:
        print(r)


if __name__ == '__main__':
    main(argv[1], argv[2], argv[3])
