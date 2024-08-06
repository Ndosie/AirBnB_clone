#!/usr/bin/python3
"""Defines unit tests for Amenity class"""
import unittest
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """Tests Instantation of Amenity class"""

    def test_unique_id(self):
        a1 = Amenity()
        a2 = Amenity()
        self.assertNotEqual(a1.id, a2.id)

    def test_str_id(self):
        a = Amenity()
        self.assertEqual(str, type(a.id))

    def test_name(self):
        self.assertEqual(type(Amenity.name), str)
