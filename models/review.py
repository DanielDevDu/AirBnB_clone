#!/usr/bin/python3
""" Class Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class Review"""

    place_id = ""  # it will be the Place.id
    user_id = ""  # it will be the User.id
    text = ""
