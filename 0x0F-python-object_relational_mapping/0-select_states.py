#!/usr/bin/python3
"""Show states in database."""
import MySQLdb as s
from sys import argv


def main(user, passw, db):
    """Show states in database and print result in order."""
    db = s.connect(host='localhost', user=user, passwd=passw, db=db, port=3306)
    c = db.cursor()
    c.execute("""SELECT id, name FROM states ORDER BY id;""")
    res = c.fetchall()
    for r in res:
        print(r)


if __name__ == '__main__':
    main(argv[1], argv[2], argv[3])
