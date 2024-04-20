#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import Column, Float, String, Table, Integer, ForeignKey
from sqlalchemy.orm import relationship
import models
from os import getenv


class Place(BaseModel, Base):
    """ Defines place class"""
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """Gets list of all linked Reviews."""
            review_list = []
            for rev in list(models.storage.all(Review).values()):
                if rev.place_id == self.id:
                    review_list.append(rev)
            return review_list

    @property
    def amenities(self):
        """Get/set linked Amenities."""
        amenity_list = []
        for ame in list(models.storage.all(Amenity).values()):
            if ame.id in self.amenity_ids:
                amenity_list.append(ame)
                return amenity_list

    @amenities.setter
    def amenities(self, value):
        if type(value) == Amenity:
            self.amenity_ids.append(value.id)
