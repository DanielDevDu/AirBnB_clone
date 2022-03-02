#!/usr/bin/python3
""" Class FileStorage"""

from email.policy import default
from models.base_model import BaseModel
import json
from os import path
import datetime
from json import JSONEncoder


# subclass JSONEncoder
class DateTimeEncoder(JSONEncoder):
    # Override the default method
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()


class FileStorage:
    """
    class that serializes instances to a JSON file
    and deserializes JSON file to instances:
    """

    __file_path = "file.json"
    __objects = {}
    __current_dict = {}

    def all(self):
        """Public instance, return dictionary"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.__dict__["id"]
        #print("__Objects: {}".format(self.__objects))
        new_dict = {key: obj}
        self.__objects.update(new_dict)
        #print("__Objects: {}".format(self.__objects))
        """
        if obj is not None:
            key = obj.__class.__name__ + "." + obj.__class.__name__.id
            self.__objects[key] = obj"""

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        # print(self.__objects)
        for key, value in self.__objects.items():
            #print("tyoe value: {}".format(type(value)))
            #print("in loop: {}".format(value.to_dict()))
            # self.__current_dict = value.to_dict()
            new_dict.update({key: value.to_dict()})

        with open(self.__file_path, mode="w+", encoding="utf-8") as file:
            json.dump(new_dict, file, cls=DateTimeEncoder)

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
