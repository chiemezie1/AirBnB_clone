#!/usr/bin/python3
"""

Module Defining User Class

"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User Class that inherits from BaseModel

    Attributes:
            email (str): user email
            password (str): user password
            first_name (str): user first name
            last_name (str): user last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Constructor for User Class """
        super().__init__(*args, **kwargs)
