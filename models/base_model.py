#!/usr/bin/python3
""" Defines a BaseModel """
import uuid
from datetime import datetime
import models


class BaseModel:
    """ Defines a BaseModel class """

    def __init__(self, *args, **kwargs):
        """
        Constructor:

        Args:
            args: the number of arguments in the program
            kwargs: a double pointer to a dictionary
        """

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k == "created_at" or k == "updated_at":
                        v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Print: [<class name>] (<self.id>) <self.__dict__> """

        cls_name = type(self).__name__
        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)

    def save(self):
        """
            Updates the public instance attribute updated_at with the
            current datetime
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
            Returns a dictionary containing all
            keys/values of __dict__ of the instance
        """

        new = self.__dict__.copy()
        new["__class__"] = type(self).__name__
        new["created_at"] = self.created_at.isoformat()
        new["updated_at"] = self.updated_at.isoformat()
        return new
