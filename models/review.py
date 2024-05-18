#!/usr/bin/python3
"""

Module Defining Review Class

"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review Class that inherits from BaseModel

    Attributes:
            place_id (str): place id
            user_id (str): user id
            text (str): review text
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Constructor for Review Class """
        super().__init__(*args, **kwargs)
