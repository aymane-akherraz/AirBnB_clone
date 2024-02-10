#!/usr/bin/python3
""" Define state module """
from models.base_model import BaseModel


class State(BaseModel):
    """ Define a State class

        Attributes:
           name (str): The name of the state.
    """

    name = ""
