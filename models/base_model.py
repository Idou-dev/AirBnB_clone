#!/usr/bin/python3
"""
BaseModel - Module
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    BaseModel class Parent class to take care of the initialization,
    """
    def __init__(self, *args, **kwargs):
        """constructor"""
        if (len(kwargs) != 0):
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            for key, val in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """String representation of a BaseModel instance"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def __repr__(self):
        """
            Return string representation of BaseModel class
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """updates 'updated_at' instance with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return dictionary representation of BaseModel class."""
        dictionnary = dict(self.__dict__)
        dictionnary['__class__'] = self.__class__.__name__
        dictionnary['created_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dictionnary['updated_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")

        return (dictionnary)
