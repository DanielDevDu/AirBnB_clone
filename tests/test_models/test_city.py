#!/usr/bin/python3
""" Unittest for City """
import unittest
from models.city import City


city_inst = City()


class test_city(unittest.TestCase):
    """Imports Class City"""

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
