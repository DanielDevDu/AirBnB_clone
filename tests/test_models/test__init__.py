#!/usr/bin/python3
""" Unittest for __init__.py"""

import unittest
from models.__init__ import storage
import pycodestyle as pep8
import os


class test__init__(unittest.TestCase):
    """IMports __init__ file"""

    def test_pep8__init__(self):
        """Test that checks for PEP8"""
        syntax = pep8.StyleGuide(quit=True)
        result = syntax.check_files(["models/__init__.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_storage(self):
        """Checks if the variable storage exits"""
        self.assertTrue(storage), True
