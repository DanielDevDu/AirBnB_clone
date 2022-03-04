#!/usr/bin/python3
""" Unittest for User """
import unittest
from models.user import User
import pycodestyle as pep8
import os

user_inst = User()


class test_user(unittest.TestCase):
    """Imports Class User"""

    def test_pep8_User(self):
        """Test that checks for PEP8"""
        syntax = pep8.StyleGuide(quit=True)
        result = syntax.check_files(["models/user.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

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
        self.assertTrue(hasattr(user_inst, "last_name"), True)

    def test_exist_file_json(self):
        """Test that check if the file.json was create"""
        path = "file.json"
        new = User()
        self.assertTrue(os.path.isfile(path))

    def test_model_from_dict(self):
        """Test that check if two objects are equals"""
        new_dict = user_inst.to_dict()
        new_user = User(**new_dict)
        self.assertNotEqual(user_inst, new_user)
