#!/usr/bin/python3
""" Unittest for User """
import unittest
from models.user import User


user_inst = User()


class test_user(unittest.TestCase):
    """Imports Class User"""

    def test_obj(self):
        """Tests if user_inst is an instance of Place"""
        self.assertIsInstance(user_inst, User)

    def test_id(self):
        """Tests if id is an instance attribute of user_inst"""
        self.assertTrue(hasattr(user_inst, "id"), True)

    def test_created_at(self):
        """Tests if created_at is an instance attribute of user_inst"""
        self.assertTrue(hasattr(user_inst, "created_at"), True)

    def test_updated_at(self):
        """Tests if updated_at is an instance attribute of user_inst"""
        self.assertTrue(hasattr(user_inst, "updated_at"), True)

    def test_save(self):
        """Tests if save is a method of user_inst"""
        self.assertTrue(hasattr(user_inst, "save"), True)

    def test_to_dict(self):
        """Tests if to_dict is a method of user_inst"""
        self.assertTrue(hasattr(user_inst, "to_dict"), True)

    def test_email(self):
        """Tests if email is an attribute of user_inst"""
        self.assertTrue(hasattr(user_inst, "email"), True)

    def test_password(self):
        """Tests if password is an attribute of user_inst"""
        self.assertTrue(hasattr(user_inst, "password"), True)

    def test_first_name(self):
        """Tests if first_name is an attribute of user_inst"""
        self.assertTrue(hasattr(user_inst, "first_name"), True)

    def test_last_name(self):
        """Tests if last_name is an attribute of user_inst"""
        self.assertTrue(hasattr(user_inst "last_name"), True)
