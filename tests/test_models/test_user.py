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
        User.email = 'user1@gmail.com'
        self.assertEqual(User.email, 'user1@gmail.com')

    def test_password(self):
        User.password = '********'
        self.assertEqual(User.password, '********')

    def test_first_name(self):
        User.first_name = 'Carrie'
        self.assertEqual(User.first_name, 'Carrie')
    
    def test_last_name(self):
        User.last_name = 'Sanga'
        self.assertEqual(User.last_name, 'Sanga')
