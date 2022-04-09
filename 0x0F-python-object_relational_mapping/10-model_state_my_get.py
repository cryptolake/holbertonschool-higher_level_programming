#!/usr/bin/python3
"""Database operations using ORM."""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main(user, passw, db, name):
    """Find state in database and print it's id."""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, passw, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    res = session.query(State).filter_by(name=name).first()
    if res:
        print(res.id)
    else:
        print("Not found")


if __name__ == '__main__':
    main(argv[1], argv[2], argv[3], argv[4])
