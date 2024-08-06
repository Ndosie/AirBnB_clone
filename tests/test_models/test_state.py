#!/usr/bin/python3
"""Defines unit tests for State class"""
import unittest
from models.state import State


class TestState_instantiation(unittest.TestCase):
    """Tests Instantation of State class"""

    def test_unique_id(self):
        s1 = State()
        s2 = State()
        self.assertNotEqual(s1.id, s2.id)

    def test_str_id(self):
        s = State()
        self.assertEqual(str, type(s.id))

    def test_name(self):
        self.assertEqual(type(State.name), str)
