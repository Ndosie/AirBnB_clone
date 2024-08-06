#!/usr/bin/python3
"""Defines unit tests for Place class"""
import unittest
from models.place import Place


class TestUser_instantiation(unittest.TestCase):
    """Tests Instantation of Place class"""

    def test_unique_id(self):
        p1 = Place()
        p2 = Place()
        self.assertNotEqual(p1.id, p2.id)

    def test_str_id(self):
        p = Place()
        self.assertEqual(str, type(p.id))

    def test_city_id(self):
        self.assertEqual(type(Place.city_id), str)

    def test_user_id(self):
        self.assertEqual(type(Place.user_id), str)

    def test_name(self):
        self.assertEqual(type(Place.name), str)
    
    def test_description(self):
        self.assertEqual(type(Place.description), str)

    def test_rooms(self):
        self.assertEqual(type(Place.number_rooms), int)

    def test_bathrooms(self):
        self.assertEqual(type(Place.number_bathrooms), int)

    def test_guest(self):
        self.assertEqual(type(Place.max_guest), int)
    
    def test_price(self):
        self.assertEqual(type(Place.price_by_night), int)

    def test_latitude(self):
        self.assertEqual(type(Place.latitude), float)

    def test_longitude(self):
        self.assertEqual(type(Place.longitude), float)
    
    def test_amenity(self):
        self.assertEqual(type(Place.amenity_ids), list)
