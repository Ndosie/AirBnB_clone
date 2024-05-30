#!/usr/bin/python3
"""Defines unit tests for BaseModel class"""

import io
import sys
import unittest
import time
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Tests instantiation of BaseModel class"""

    def test_unique_id(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_str_id(self):
        b = BaseModel()
        self.assertEqual(str, type(b.id))

    def test_created_at(self):
        b = BaseModel()
        self.assertEqual(type(b.created_at), datetime)


class TestBaseModel_save(unittest.TestCase):
    """Tests save method of BaseModel class"""

    def test_updated_at(self):
        b = BaseModel()
        before = b.updated_at
        time.sleep(10)
        b.save()
        self.assertNotEqual(b.update_at, before)


class TestBaseModel_to_dict(unittest.TestCase):
    """Tests to_dict method of BaseModel class"""

    def test_to_dict(self):
        b = BaseModel()
        dict_b = b.to_dict()
        self.assertEqual(type(dict_b['created_at']), str)


class TestBaseModel__str__(unittest.TestCase):
    """Tests __str__ method of BaseModel class"""
    
    @staticmethod
    def capture_stdout(obj):
        capture = io.StringIO()
        sys.stdout = capture
        obj.__str__()
        sys.stdout = sys.__stdout__
        return capture

    def test__str__(self):
        b = BaseModel()
        output = TestBaseModel__str__.capture_stdout(b)
        self.assertTrue(b.__class__.__name__ in output.getvalue())
