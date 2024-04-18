#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    name = ""
    def __init__(self, *args, **kwargs):
        """Initialization"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """String representation"""
        return "[State] ({}) {}".format(self.id, self.to_dict())

