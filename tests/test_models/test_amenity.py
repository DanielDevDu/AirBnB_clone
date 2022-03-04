#!/usr/bin/python3
""" Unittest for Amenity """
import unittest
from models.amenity import Amenity
import pycodestyle as pep8
import os

Amenity_inst = Amenity()


class test_amenity(unittest.TestCase):
    """Imports Class Amenity"""

    def test_pep8_Amenity(self):
        """Test that checks for PEP8"""
        syntax = pep8.StyleGuide(quit=True)
        result = syntax.check_files(["models/amenity.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

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

    def test_exist_file_json(self):
        """Test that check if the file.json was create"""
        path = "file.json"
        new = Amenity()
        self.assertTrue(os.path.isfile(path))

    def test_model_from_dict(self):
        """Test that check if two objects are equals"""
        new_dict = Amenity_inst.to_dict()
        new_amenity = Amenity(**new_dict)
        self.assertNotEqual(Amenity_inst, new_amenity)
