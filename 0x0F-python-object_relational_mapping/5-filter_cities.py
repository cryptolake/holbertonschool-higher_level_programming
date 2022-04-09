#!/usr/bin/python3
"""Show states in database."""
import MySQLdb as sql
from sys import argv


def main(user, passw, db, state):
    """Show cities of state in database and print result in order."""
    db = sql.connect(host='localhost', user=user,
                     passwd=passw, db=db, port=3306)
    c = db.cursor()
    c.execute("""
            SELECT c.name
            FROM cities c
            INNER JOIN states s ON s.id = c.state_id
            WHERE s.name = %s
            ORDER BY c.id;
            """, (state,))
    res = c.fetchall()
    arr = []
    for r in res:
        arr.append(r[0])
    print(', '.join(arr))


if __name__ == '__main__':
    main(argv[1], argv[2], argv[3], argv[4])
