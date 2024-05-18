#!/usr/bin/python3
"""

Module Defining City Class

"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City Class that inherits from BaseModel

    Attributes:
        state_id (str): state id
        name (str): city name
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Constructor for City Class """
        super().__init__(*args, **kwargs)
