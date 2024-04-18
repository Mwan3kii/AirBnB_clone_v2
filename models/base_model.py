#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
import models
import os


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            if 'id' not in kwargs:
                kwargs['id'] = str(uuid.uuid4())
            for key in ['created_at', 'updated_at']:
                if key in kwargs:
                    try:
                        kwargs[key] = datetime.strptime(kwargs[key], '%Y-%m-%dT%H:%M:%S.%f')
                    except ValueError:
                        print(f"Invalid format for {key}: {kwargs[key]}")
                        del kwargs[key]
            if 'created_at' not in kwargs:
                kwargs['created_at'] = datetime.now()
            if 'updated_at' not in kwargs:
                    kwargs['updated_at'] = datetime.now()
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def delete(self):
        """Deletes the instance from the storage"""
        from models import storage
        storage.delete(self)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        new_dict = {}
        for key, value in self.__dict__.items():
            if key != '_sa_instance_state':
                if isinstance(value, datetime):
                    new_dict[key] = value.isoformat()
                else:
                    new_dict[key] = value
        new_dict['__class__'] = self.__class__.__name__
        return new_dict
