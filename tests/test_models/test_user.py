#!/usr/bin/python3
"""Defines unit tests for User class"""
import unittest
from models.user import User


class TestUser_instantiation(unittest.TestCase):
    """Tests Instantation of User class"""

    def test_unique_id(self):
        u1 = User()
        u2 = User()
        self.assertNotEqual(u1.id, u2.id)

    def test_str_id(self):
        u = User()
        self.assertEqual(str, type(u.id))

    def test_email(self):
        self.assertEqual(type(User.email), str)

    def test_password(self):
        self.assertEqual(type(User.password), str)

    def test_first_name(self):
        self.assertEqual(type(User.first_name), str)
    
    def test_last_name(self):
        self.assertEqual(type(User.last_name), str)
