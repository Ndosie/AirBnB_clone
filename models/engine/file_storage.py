#!/usr/bin/python3
"""Defines FileStorage class"""
import json


class FileStorage:
    """Serializes instances to JSON and deserialize it to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns objects"""
        return __objects
    
    def new(self, obj):
        """Sets objects"""
        __objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """Serializes objects to JSON file"""
        with open(__file_path, mode='w') as f:
            f.write(json.dumps(__objects))

    def reload(self):
        """Deserializees Json to objects"""
        try:
            with open(__file_path, mode='r') as f:
                __objects = json.loads(f.read())
        except FILENOTFOUNDERROR:
            pass
