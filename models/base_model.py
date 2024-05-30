#!/usr/bin/python3

"""Define a Base class"""
from datetime import datetime
import uuid
import storage


class BaseModel:
    """Base model.
    This class represent the base of all classes in AirBnB project
    """

    def __init__(self, *args, **kwargs):
        """Initializes a new Base instance"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs and len(kwargs) != 0:
            for k,v in kwargs.items():
                if k != '__class__':
                    if k == 'created_at' or k == 'updated_at':
                        self.__dict__[k] = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f") 
                    else:
                        self.__dict__[k] = v
        else:
            storage.new(self)

    def __str__(self):
        """Prints the string representation of an object"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the update_at attribute"""
        self.update_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns dictionary containing all the keys/values"""
        dict_b = self.__dict__
        dict_b['__class__'] = self.__class__.__name__
        dict_b['created_at'] = datetime.isoformat(self.created_at)
        dict_b['updated_at'] = datetime.isoformat(self.updated_at)

        return dict_b
