#!/usr/bin/python3
""" Unittest for Review """
import unittest
from models.review import Review


review_inst = Review()


class test_review(unittest.TestCase):
    """Imports Class Review"""

    def test_obj(self):
        """Tests if review_inst is an instance of Review"""
        self.assertIsInstance(review_inst, Review)

    def test_id(self):
        """Tests if id is an instance attribute of review_inst"""
        self.assertTrue(hasattrreview_inst, "id"), True)

    def test_created_at(self):
        """Tests if created_at is an instance attribute of review_inst"""
        self.assertTrue(hasattr(review_inst, "created_at"), True)

    def test_updated_at(self):
        """Tests if updated_at is an instance attribute of review_inst"""
        self.assertTrue(hasattr(review_inst, "updated_at"), True)

    def test_save(self):
        """Tests if save is a method of review_inst"""
        self.assertTrue(hasattr(review_inst, "save"), True)

    def test_to_dict(self):
        """Tests if to_dict is a method of review_inst"""
        self.assertTrue(hasattr(review_inst, "to_dict"), True)

    def test_place_id(self):
        """Tests if place_id is an attribute of review_inst"""
        self.assertTrue(hasattr(review_inst, "place_id"), True)

    def test_user_id(self):
        """Tests if user_id is an attribute of review_inst"""
        self.assertTrue(hasattr(review_inst, "user_id"), True)

    def test_text(self):
        """Tests if text is an attribute of obj_Review"""
        self.assertTrue(hasattr(review_inst, "text"), True)
