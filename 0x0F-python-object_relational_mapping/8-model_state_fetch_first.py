#!/usr/bin/python3
"""List first state using ORM."""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main(user, passw, db):
    """List first state in database and print result in order."""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, passw, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    first_state = session.query(State).first()
    if first_state:
        print("{:d}: {:s}".format(first_state.id, first_state.name))
    else:
        print("Nothing")


if __name__ == '__main__':
    main(argv[1], argv[2], argv[3])
