#!/usr/bin/python3
"""
Unittest for Place class
"""

import unittest

import models

from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for the Place class"""

    def setUp(self):
        """Set up for the tests"""
        self.place = Place()
        self.place.city_id = "opo lopo"
        self.place.user_id = "sñfjefpa"
        self.place.name = "My house"

    def test_init(self):
        """Test the initialization of the Place instance"""
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)

    def test_instance(self):
        """Test for Place instance"""
        instance = Place()
        self.assertIsInstance(instance, Place)

    def test_city_id(self):
        """Test for Place city_id"""
        instance = Place()
        self.assertIsInstance(instance.city_id, str)

    def test_user_id(self):
        """Test for Place user_id"""
        instance = Place()
        self.assertIsInstance(instance.user_id, str)

    def test_name(self):
        """Test for Place name"""
        instance = Place()
        self.assertIsInstance(instance.name, str)

    def test_str(self):
        """Test for __str__ method"""
        self.assertEqual(str(self.place), "[Place] ({}) {}".format(
            self.place.id, self.place.__dict__))

    def test_to_dict(self):
        """Test for to_dict method"""
        self.assertIsInstance(self.place.to_dict(), dict)


if __name__ == "__main__":
    unittest.main()
