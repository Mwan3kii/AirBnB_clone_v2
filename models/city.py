#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """ The city class inherits from BaseModel and Base"""
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    state = relationship("State", back_populates="cities")
    places = relationship('Place', backref='cities', cascade='all, delete')

    def __init__(self, *args, **kwargs):
        """Initialization method for City"""
        super().__init__(*args, **kwargs)
