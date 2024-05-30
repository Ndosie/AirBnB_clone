#!/usr/bin/python3
"""Defines FileStorage class"""
import json


class FileStorage:
    """Serializes instances to JSON and deserialize it to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        """Sets objects"""
        class_n = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(class_n, obj.id)] = obj

    def save(self):
        """Serializes objects to JSON file"""
        with open(FileStorage__file_path, mode='w') as f:
            f.write(json.dumps(FileStorage.__objects))

    def reload(self):
        """Deserializees Json to objects"""
        try:
            with open(FileStorage__file_path, mode='r') as f:
                FileStorage.__objects = json.loads(f.read())
        except FILENOTFOUNDERROR:
            return
