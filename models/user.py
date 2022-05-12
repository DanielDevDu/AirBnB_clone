#!/usr/bin/python3
""" Class User"""

from models.base_model import BaseModel


class User(BaseModel):
    """Class User"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """User initialization"""
        super().__init__(*args, **kwargs)
