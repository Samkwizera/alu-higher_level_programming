#!/usr/bin/python3
"""Unittest for Rectangle class."""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def test_attributes(self):
        """Test rectangle attributes."""
        r1 = Rectangle(10, 2, 1, 1, 12)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r1.id, 12)
