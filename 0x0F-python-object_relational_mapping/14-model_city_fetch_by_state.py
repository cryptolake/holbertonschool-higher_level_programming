#!/usr/bin/python3
"""Database operations using ORM."""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main(user, passw, db):
    """Print all Cities in states."""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, passw, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City, State).join(State).all()
    for city in cities:
        print("{:s}: ({:d}) {:s}".format(city[1].name,
                                         city[0].id, city[0].name))


if __name__ == '__main__':
    main(argv[1], argv[2], argv[3])
