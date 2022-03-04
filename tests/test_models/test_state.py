#!/usr/bin/python3
""" Unittest for State """
import unittest
from models.state import State
import pycodestyle as pep8
import os

state_inst = State()


class test_state(unittest.TestCase):
    """Imports Class State"""

    def test_pep8_State(self):
        """Test that checks for PEP8"""
        syntax = pep8.StyleGuide(quit=True)
        result = syntax.check_files(["models/state.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_obj(self):
        """Tests if state_inst is an instance of State"""
        self.assertIsInstance(state_inst, State)

    def test_obj_name(self):
        """Checks if name is an atribute of state_inst"""
        self.assertTrue(hasattr(state_inst, "name"), True)

    def test_State_name(self):
        """Checks if name is an atribute of State"""
        self.assertTrue(hasattr(State, "name"), True)

    def test_id(self):
        """Tests if id is an instance attribute of state_inst"""
        self.assertTrue(hasattr(state_inst, "id"), True)

    def test_created_at(self):
        """Tests if created_at is an instance attribute of state_inst"""
        self.assertTrue(hasattr(state_inst, "created_at"), True)

    def test_updated_at(self):
        """Tests if updated_at is an instance attribute of state_inst"""
        self.assertTrue(hasattr(state_inst, "updated_at"), True)

    def test_save(self):
        """Tests if save is a method of state_inst"""
        self.assertTrue(hasattr(state_inst, "save"), True)

    def test_to_dict(self):
        """Tests if to_dict is a method of state_inst"""
        self.assertTrue(hasattr(state_inst, "to_dict"), True)

    def test_name(self):
        """Tests if name is an attribute of state_inst"""
        self.assertTrue(hasattr(state_inst, "name"), True)

    def test_exist_file_json(self):
        """Test that check if the file.json was create"""
        path = "file.json"
        new = State()
        self.assertTrue(os.path.isfile(path))

    def test_model_from_dict(self):
        """Test that check if two objects are equals"""
        new_dict = state_inst.to_dict()
        new_state = State(**new_dict)
        self.assertNotEqual(state_inst, new_state)
