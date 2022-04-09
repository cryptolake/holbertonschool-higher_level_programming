#!/usr/bin/python3
"""List all states using ORM."""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main(user, passw, db):
    """List states that contain a in database and print result in order."""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, passw, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).order_by(State.id):
        if 'a' in state.name:
            print("{:d}: {:s}".format(state.id, state.name))


if __name__ == '__main__':
    main(argv[1], argv[2], argv[3])
