#!/usr/bin/python3
"""

Module Defining Amenity Class

"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity Class that inherits from BaseModel

    Attributes:
            name (str): amenity name
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Constructor for Amenity Class """
        super().__init__(*args, **kwargs)
