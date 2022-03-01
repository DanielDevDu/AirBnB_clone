#!/usr/bin/python3
""" Class BaseModel"""

import uuid
from datetime import datetime


class BaseModel:
    """Class BaseModel that defines all common
    attributes/methods for other classes"""
    def __init__(self):
        """Initialization of the base model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returns a dictorionary of all keys and values of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat
        new_dict["updated_at"] = new_dict["updated_at"].isoformat
        return new_dict
