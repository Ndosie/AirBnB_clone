#!/usr/bin/python3
"""Defines FileStorage class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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
        dict_o = FileStorage.__objects
        o_to_dict = {k: v.to_dict() for k, v in dict_o.items()}
        with open(FileStorage.__file_path, mode='w') as f:
            json.dump(o_to_dict, f)

    def reload(self):
        """Deserializes Json to objects"""
        try:
            with open(FileStorage.__file_path, mode='r') as f:
                o_to_dict = json.loads(f.read())
                for obj in o_to_dict.values():
                    c_name = obj['__class__']
                    self.new(eval(c_name)(**obj))
        except FileNotFoundError:
            return
