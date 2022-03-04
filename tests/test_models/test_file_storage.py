#!/usr/bin/python3
""" Unittest for FileStorage"""
import unittest
from models.engine.file_storage import FileStorage


file_inst = FileStorage()


class test_file_storage(unittest.TestCase):
    """Imports Class FileStorage"""

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

    def test_reload(self):
        """Test if reload is a method of file_inst"""
        self.assertTrue(hasattr(file_inst, "reload"), True)
