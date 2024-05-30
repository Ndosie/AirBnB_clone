#!/usr/bin/python3
"""Defines tests for FileStorage class"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage_instatiation(unittest.TestCase):
    """Tests initalization of FileStorage class"""

    def test__objects(self):
        b = BaseModel()
        objs = FileStorage().all()
        self.assertEqual(objs["BaseModel.{}".format(b.id)], b)


class TestFileStorage_all(unittest.TestCase):
    """Tests all method of FileStorage class"""

    def test_all(self):
        b1 = BaseModel()
        b2 = BaseModel()
        objs = FileStorage().all()
        self.assertEqual(len(objs), 2)


class TestFileStorage_new(unittest.TestCase):
    """Tests new method of FileStorage class"""

    def test_new(self):
        b = BaseModel()
        FileStorage().new(b)
        objs = FileStorage().all()
        self.assertEqual(objs["BaseModel.{}".format(b.id)], b)


class TestFileStorage_save(unittest.TestCase):
    """Tests save method of FileStorage class"""

    def test_save(self):
        b = BaseModel()
        FileStorage().save()
        with open('file.json', m='r') as f:
            contents = f.read()
        self.assertEqual(b.id)
