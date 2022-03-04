#!/usr/bin/python3
""" Unittest for City """
import unittest
from models.city import City
import pycodestyle as pep8
import os

city_inst = City()


class test_city(unittest.TestCase):
    """Imports Class City"""

    def test_pep8_City(self):
        """Test that checks for PEP8"""
        syntax = pep8.StyleGuide(quit=True)
        result = syntax.check_files(["models/city.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_obj(self):
        """Tests if city_inst is an instance of City"""
        self.assertIsInstance(city_inst, City)

    def test_obj_name(self):
        """Checks if name is an atribute of city_inst"""
        self.assertTrue(hasattr(city_inst, "name"), True)

    def test_City_name(self):
        """Checks if name is an atribute of City"""
        self.assertTrue(hasattr(City, "name"), True)

    def test_id(self):
        """Tests if id is an instance attribute of city_inst"""
        self.assertTrue(hasattr(city_inst, "id"), True)

    def test_created_at(self):
        """Tests if created_at is an instance attribute of city_inst"""
        self.assertTrue(hasattr(city_inst, "created_at"), True)

    def test_updated_at(self):
        """Test if updated_at is an instance attribute of city_inst"""
        self.assertTrue(hasattr(city_inst, "updated_at"), True)

    def test_save(self):
        """Test if save is a method of city_inst"""
        self.assertTrue(hasattr(city_inst, "save"), True)

    def test_to_dict(self):
        """Test if to_dict is a method of city_inst"""
        self.assertTrue(hasattr(city_inst, "to_dict"), True)

    def test_exist_file_json(self):
        """Test that check if the file.json was create"""
        path = "file.json"
        new = City()
        self.assertTrue(os.path.isfile(path))

    def test_model_from_dict(self):
        """Test that check if two objects are equals"""
        new_dict = city_inst.to_dict()
        new_city = City(**new_dict)
        self.assertNotEqual(city_inst, new_city)
