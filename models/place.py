#!/usr/bin/python3
"""

Module Defining Place Class

"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place Class that inherits from BaseModel

    Attributes:
        city_id (str): city id
        user_id (str): user id
        name (str): place name
        description (str): place description
        number_rooms (int): number of rooms
        number_bathrooms (int): number of bathrooms
        max_guest (int): max number of guests
        price_by_night (int): price by night
        latitude (float): place latitude
        longitude (float): place longitude
        amenity_ids (list): list of amenity ids
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Constructor for Place Class """
        super().__init__(*args, **kwargs)
