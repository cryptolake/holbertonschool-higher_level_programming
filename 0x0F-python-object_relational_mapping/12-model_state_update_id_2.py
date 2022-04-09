#!/usr/bin/python3
"""Database operations using ORM."""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main(user, passw, db):
    """Edit row where id = 2 in Database."""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, passw, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    upstate = session.query(State).filter(State.id == 2).first()
    upstate.name = "New Mexico"
    session.commit()


if __name__ == '__main__':
    main(argv[1], argv[2], argv[3])
