#!/usr/bin/python3
"""Defines unit tests for Review class"""
import unittest
from models.review import Review


class TestUser_instantiation(unittest.TestCase):
    """Tests Instantation of Review class"""

    def test_unique_id(self):
        r1 = Review()
        r2 = Review()
        self.assertNotEqual(r1.id, r2.id)

    def test_str_id(self):
        r = Review()
        self.assertEqual(str, type(r.id))

    def test_place_id(self):
        self.assertEqual(type(Review.place_id), str)

    def test_user_id(self):
        self.assertEqual(type(Review.user_id), str)

    def test_text(self):
        self.assertEqual(type(Review.text), str)
