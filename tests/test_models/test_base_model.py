#!/usr/bin/python3
""" Unittest for BaseModel """
import unittest
import pycodestyle as pep8
import os
from models.base_model import BaseModel
import json

base_instance = BaseModel()


class test_base_model(unittest.TestCase):
    """Imports class BaseModel"""

    def test_pep8_base(self):
        """Test that checks for PEP8"""
        syntax = pep8.StyleGuide(quit=True)
        result = syntax.check_files(["models/base_model.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_base_instance(self):
        """Checks if base_instance is a BaseModel instance"""
        self.assertIsInstance(base_instance, BaseModel)

    def test_id(self):
        """Tests if id is an instance attribute of BaseModel"""
        self.assertTrue(hasattr(base_instance, "id"), True)

    def test_created_at(self):
        """Tests if created_at is an instance attribute of BaseModel"""
        self.assertTrue(hasattr(base_instance, "created_at"), True)

    def test_updated_at(self):
        """Tests if updated_at is an instance attribute of BaseModel"""
        self.assertTrue(hasattr(base_instance, "updated_at"), True)

    def test_save1(self):
        """Tests to check if the date is updating"""
        temp1 = base_instance.updated_at
        base_instance.save()
        temp2 = base_instance.updated_at
        self.assertNotEqual(temp1, temp2)

    def test_save_2(self):
        """Tests if save is a method of BaseModel"""
        self.assertTrue(hasattr(BaseModel, "save"), True)

    def test_to_dict1(self):
        """Tests if to_dict is a dictionary"""
        new_dict = base_instance.to_dict()
        self.assertIsInstance(new_dict, dict)

    def test_to_dict_2(self):
        """Tests if to_dict is a method of BaseModel"""
        self.assertTrue(hasattr(BaseModel, "to_dict"), True)

    def test_to_str(self):
        """Tests if __str__ is a method of BaseModel"""
        self.assertTrue(hasattr(BaseModel, "__str__"), True)

    def test__str__(self):
        """Tests if __str__ is a string"""
        str1 = base_instance.__str__()
        self.assertTrue(type(str1) is str)

    def test_model_from_dict(self):
        """Test if an object created from a dict is an instance"""
        new_dict = base_instance.to_dict()
        new_base = BaseModel(**new_dict)
        self.assertIsInstance(new_base, BaseModel)

    def test_model_from_dict_2(self):
        """Test that check if two objects are equals"""
        new_dict = base_instance.to_dict()
        new_base = BaseModel(**new_dict)
        self.assertNotEqual(base_instance, new_base)

    def test_exist_file_json(self):
        """Test that check if the file.json was create"""
        path = "file.json"
        new = BaseModel()
        self.assertTrue(os.path.isfile(path))
