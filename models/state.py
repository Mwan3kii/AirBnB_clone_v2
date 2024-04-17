#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class inherits from BaseModel and Base"""
    name = Column(String(128), nullable=False)
    __tablename__ = 'states'
    cities = relationship("City", cascade="all, delete", backref="state")

    def __init__(self, *args, **kwargs):
        """Initialization method for State"""
        super().__init__(*args, **kwargs)
