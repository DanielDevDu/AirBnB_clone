#!/usr/bin/python3
""" Class Amenity"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class Amenity"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Amenity initialization"""
        super().__init__(*args, **kwargs)