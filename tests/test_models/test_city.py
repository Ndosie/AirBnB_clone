#!/usr/bin/python3
"""Defines unit tests for City class"""
import unittest
from models.city import City


class TestCity_instantiation(unittest.TestCase):
    """Tests Instantation of City class"""

    def test_unique_id(self):
        c1 = City()
        c2 = City()
        self.assertNotEqual(c1.id, c2.id)

    def test_str_id(self):
        c = City()
        self.assertEqual(str, type(c.id))

    def test_state_id(self):
        self.assertEqual(type(City.state_id), str)

    def test_name(self):
        self.assertEqual(type(City.name), str)
