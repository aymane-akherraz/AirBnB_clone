#!/usr/bin/python3
""" Define city module """
from models.base_model import BaseModel


class City(BaseModel):
    """ Define a City class """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Constructor:

        Args:
            args: the number of arguments in the program
            kwargs: a double pointer to a dictionary
        """
        super().__init__(*args, **kwargs)

    def __str__(self):
        """ Print: [<class name>] (<self.id>) <self.__dict__> """

        return super().__str__()

    def save(self):
        """
            Updates the public instance attribute updated_at with the
            current datetime
        """
        super().save()

    def to_dict(self):
        """
            Returns a dictionary containing all
            keys/values of __dict__ of the instance
        """
        return super().to_dict()
