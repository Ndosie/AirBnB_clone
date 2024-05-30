#!/usr/bin/python3

"""Define a Base class"""
from datetime import datetime
import uuid


class BaseModel:
    """Base model.
    This class represent the base of all classes in AirBnB project
    """

    def __init__(self):
        """Initializes a new Base instance"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Prints the string representation of an object"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the update_at attribute"""
        self.update_at = datetime.now()

    def to_dict(self):
        """Returns dictionary containing all the keys/values"""
        dict_b = self.__dict__
        dict_b['__class__'] = self.__class__.__name__
        dict_b['created_at'] = datetime.isoformat(self.created_at)
        dict_b['updated_at'] = datetime.isoformat(self.updated_at)

        return dict_b
