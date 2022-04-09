#!/usr/bin/python3
"""Represent the state table using a class."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State object orm."""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                autoincrement=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
