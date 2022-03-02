#!/usr/bin/python3
""" Class FileStorage"""

from models.base_model import BaseModel
import json
from os import path


class FileStorage:
    """
    class that serializes instances to a JSON file
    and deserializes JSON file to instances:
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Public instance, return dictionary"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.__dict__["id"]
        new_dict = {key: obj}
        self.__objects.update(new_dict)
        """
        if obj is not None:
            key = obj.__class.__name__ + "." + obj.__class.__name__.id
            self.__objects[key] = obj"""

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict.update({key: value.to_dict()})

        with open(self.__file_path, mode="w+", encoding="utf-8") as file:
            json.dump(new_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as file:
                json_string = json.load(file)
                for key, value in json_string.items():
                    a = BaseModel(**value)
                    new_dict = {key: a}
                    self.__objects.update(new_dict) 
        except Exception:
            pass
