#!/usr/bin/python3
""" Define amenity module """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Define a Amenity class
        Attributes:
            name (str): The name of the amenity.
    """

    name = ""
