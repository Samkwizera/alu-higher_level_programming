#!/usr/bin/python3
"""Unittest for Base class."""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def test_id_auto_increment(self):
        """Test automatic id increment."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_custom_id(self):
        """Test custom id assignment."""
        b3 = Base(12)
        self.assertEqual(b3.id, 12)

