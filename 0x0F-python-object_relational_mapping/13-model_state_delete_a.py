#!/usr/bin/python3
"""Database operations using ORM."""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main(user, passw, db):
    """Delete all States with a from database."""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, passw, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).all()
    for state in states:
        if 'a' in state.name:
            session.delete(state)
    session.commit()


if __name__ == '__main__':
    main(argv[1], argv[2], argv[3])
