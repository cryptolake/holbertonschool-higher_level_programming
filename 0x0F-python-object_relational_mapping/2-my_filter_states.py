#!/usr/bin/python3
"""Show states in database."""
import MySQLdb as sql
from sys import argv


def main(user, passw, db, state):
    """Filter states in database and print result in order."""
    db = sql.connect(host='localhost', user=user,
                     passwd=passw, db=db, port=3306)
    c = db.cursor()
    c.execute("""
            SELECT id, name
            FROM states
            WHERE name='{}' ORDER BY id;""".format(state))
    res = c.fetchall()
    for r in res:
        print(r)


if __name__ == '__main__':
    main(argv[1], argv[2], argv[3], argv[4])
