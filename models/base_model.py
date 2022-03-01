#!/usr/bin/python3
""" Class BaseModel"""

import models
import uuid
from datetime import datetime

class BaseModel:
    """Class BaseModel that defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
            """Initialization of the base model"""
            if kwargs:
                for key, value in kwargs.items():
                    if key != "__class__":
                        setattr(self, key, value)
                if hasattr(self, "created_at") and type(self.created_at) is str:
                    self.created_at = datetime.strptime(kwargs["created_at"], time)
                if hasattr(self, "updated_at") and type(self.updated_at) is str:
                    self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = self.created_at
