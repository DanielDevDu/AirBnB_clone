#!/usr/bin/python3
""" Unittest for Amenity """
import unittest
from models.amenity import Amenity


Amenity_inst = Amenity()


class test_amenity(unittest.TestCase):
    """Imports Class Amenity"""

    def test_Amenity_inst(self):
        """Test if Amenity_inst is an Amenity instance"""
        self.assertIsInstance(Amenity_inst, Amenity)

    def test_obj_name(self):
        """Checks if name is an atribute of Amenity_inst"""
        self.assertTrue(hasattr(Amenity_inst, "name"), True)

    def test_Amenity_name(self):
        """Checks if name is an atribute of Amenity"""
        self.assertTrue(hasattr(Amenity, "name"), True)

    def test_id(self):
        """Tests if id is an instance attribute of Amenity_inst"""
        self.assertTrue(hasattr(Amenity_inst, "id"), True)

    def test_created_at(self):
        """Tests if created_at is an instance attribute of Amenity_inst"""
        self.assertTrue(hasattr(Amenity_inst, "created_at"), True)

    def test_updated_at(self):
        """Tests if updated_at is an instance attribute of Amenity_inst"""
        self.assertTrue(hasattr(Amenity_inst, "updated_at"), True)

    def test_save(self):
        """Tests if save is a method of Amenity_inst"""
        self.assertTrue(hasattr(Amenity_inst, "save"), True)

    def test_to_dict(self):
        """Tests if to_dict is a method of Amenity_inst"""
        self.assertTrue(hasattr(Amenity_inst, "to_dict"), True)
