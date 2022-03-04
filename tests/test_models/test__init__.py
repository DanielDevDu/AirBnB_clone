#!/usr/bin/python3
""" Unittest for __init__.py"""

import unittest
from models.__init__ import storage


class test__init__(unittest.TestCase):
    """IMports __init__ file"""

    def test_storage(self):
        """Checks if the variable storage exits"""
        self.assertTrue(storage), True
