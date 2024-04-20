#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
import os
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes

    Attributes:
        __tablename__ (str): Name of the MySQL table to store users.
        email: (sqlalchemy String): The user email address.
        password (sqlalchemy String): The user password.
        first_name (sqlalchemy String): The user first name.
        last_name (sqlalchemy String): The user last name.
        places (sqlalchemy relationship): The Place relationship.
        reviews (sqlalchemy relationship): The Review relationship.
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")
