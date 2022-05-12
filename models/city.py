#!/usr/bin/python3
""" Class City"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class City"""

    name = ""
    state_id = ""  # it will be the State.id

    def __init__(self, *args, **kwargs):
        """City initialization"""
        super().__init__(*args, **kwargs)
