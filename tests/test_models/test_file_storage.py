#!/usr/bin/python3
""" Unittest for FileStorage"""
import unittest
from models.engine.file_storage import FileStorage
import pycodestyle as pep8
import os
from models.base_model import BaseModel
import json


file_inst = FileStorage()
base = BaseModel()
base.save()


class test_file_storage(unittest.TestCase):
    """Imports Class FileStorage"""

    def test_pep8_FileStorage(self):
        """Test that checks for PEP8"""
        syntax = pep8.StyleGuide(quit=True)
        result = syntax.check_files(["models/engine/file_storage.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_obj(self):
        """Checks if file_inst is a FileStorage instance"""
        self.assertIsInstance(file_inst, FileStorage)

    def test_file_path(self):
        """Tests if __file_path is an instance attribute of BaseModel"""
        self.assertFalse(hasattr(FileStorage, "__file_path"), False)

    def test_file_objects(self):
        """Test if __objects is an instance attribute of BaseModel"""
        self.assertFalse(hasattr(FileStorage, "__objects"), False)

    def test_all(self):
        """Test if all is a method of file_inst"""
        self.assertTrue(hasattr(file_inst, "all"), True)

    def test_new(self):
        """Test if new is a method of file_inst"""
        self.assertTrue(hasattr(file_inst, "new"), True)

    def test_save(self):
        """Test if save is a method of file_inst"""
        self.assertTrue(hasattr(file_inst, "save"), True)

    def test_save_2(self):
        """Test that check if was save it"""
        path = "file.json"
        with open(path, mode="r", encoding="utf-8") as file:
            data_base = file.read()
        new_base = BaseModel()
        new_base.save()
        with open(path, mode="r", encoding="utf-8") as file:
            data_new_base = file.read()
        self.assertTrue(len(data_new_base) > len(data_base))

    def test_reload(self):
        """Test if reload is a method of file_inst"""
        self.assertTrue(hasattr(file_inst, "reload"), True)

    def test_exist_file_json(self):
        """Test that check if the file.json was create"""
        path = "file.json"
        self.assertTrue(os.path.isfile(path))

    def test_all_returns_dict(self):
        """Test that all returns the FileStorage.__objects attr"""
        storage = FileStorage()
        new_dict = storage.all()
        self.assertEqual(type(new_dict), dict)
        self.assertIs(new_dict, storage._FileStorage__objects)
