#!/usr/bin/python3
""" Unittest for Place """
import unittest
from models.place import Place
import pycodestyle as pep8
import os

place_inst = Place()


class test_place(unittest.TestCase):
    """Imports Class Place"""

    def test_pep8_Place(self):
        """Test that checks for PEP8"""
        syntax = pep8.StyleGuide(quit=True)
        result = syntax.check_files(["models/place.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_obj(self):
        """Tests if place_inst is an instance of Place"""
        self.assertIsInstance(place_inst, Place)

    def test_obj_name(self):
        """Checks if name is an atribute of obj_Place"""
        self.assertTrue(hasattr(place_inst, "name"), True)

    def test_Place_name(self):
        """Checks if name is an atribute of Place"""
        self.assertTrue(hasattr(Place, "name"), True)

    def test_id(self):
        """Tests if id is an instance attribute of place_inst"""
        self.assertTrue(hasattr(place_inst, "id"), True)

    def test_created_at(self):
        """Tests if created_at is an instance attribute of place_inst"""
        self.assertTrue(hasattr(place_inst, "created_at"), True)

    def test_updated_at(self):
        """Tests if updated_at is an instance attribute of place_inst"""
        self.assertTrue(hasattr(place_inst, "updated_at"), True)

    def test_save(self):
        """Tests if save is a method of place_inst"""
        self.assertTrue(hasattr(place_inst, "save"), True)

    def test_to_dict(self):
        """Tests if to_dict is a method of place_inst"""
        self.assertTrue(hasattr(place_inst, "to_dict"), True)

    def test_city_id(self):
        """Test if city_id is an attribute of place_inst"""
        self.assertTrue(hasattr(place_inst, "city_id"), True)

    def test_name(self):
        """Test if name is an attribute of place_inst"""
        self.assertTrue(hasattr(place_inst, "name"), True)

    def test_description(self):
        """Test if description is an attribute of place_inst"""
        self.assertTrue(hasattr(place_inst, "description"), True)

    def test_number_rooms(self):
        """Test if number_rooms is an attribute of place_inst"""
        self.assertTrue(hasattr(place_inst, "number_rooms"), True)

    def test_number_bathrooms(self):
        """Test if number_bathrooms is an attribute of place_inst"""
        self.assertTrue(hasattr(place_inst, "number_bathrooms"), True)

    def test_max_guest(self):
        """Test if max_guest is an attribute of place_inst"""
        self.assertTrue(hasattr(place_inst, "max_guest"), True)

    def test_price_by_night(self):
        """Test if price_by_night is an attribute of place_inst"""
        self.assertTrue(hasattr(place_inst, "price_by_night"), True)

    def test_latitude(self):
        """Test if latitude is an attribute of place_inst"""
        self.assertTrue(hasattr(place_inst, "latitude"), True)

    def test_longitude(self):
        """Test if longitude is an attribute of place_inst"""
        self.assertTrue(hasattr(place_inst, "longitude"), True)

    def test_amenity_ids(self):
        """Test if amenity_ids is an attribute of place_inst"""
        self.assertTrue(hasattr(place_inst, "amenity_ids"), True)

    def test_exist_file_json(self):
        """Test that check if the file.json was create"""
        path = "file.json"
        new = Place()
        self.assertTrue(os.path.isfile(path))

    def test_model_from_dict(self):
        """Test that check if two objects are equals"""
        new_dict = place_inst.to_dict()
        new_place = Place(**new_dict)
        self.assertNotEqual(place_inst, new_place)
