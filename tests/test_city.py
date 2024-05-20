#!/usr/bin/python3
"""
Unittest for City class

"""

import unittest

import models

from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    def setUp(self):
        """Set up for the tests"""
        self.city = City()
        self.city.name = "San Francisco"
        self.city.state_id = "California"

    def test_init(self):
        """Test the initialization of the City instance"""
        self.assertIsInstance(self.city.name, str)
        self.assertIsInstance(self.city.state_id, str)

    def test_instance(self):
        """Test for City instance"""
        instance = City()
        self.assertIsInstance(instance, City)

    def test_name(self):
        """Test for City name"""
        instance = City()
        self.assertIsInstance(instance.name, str)

    def test_state_id(self):
        """Test for City state_id"""
        instance = City()
        self.assertIsInstance(instance.state_id, str)

    def test_str(self):
        """Test for __str__ method"""
        self.assertEqual(str(self.city), "[City] ({}) {}".format(
            self.city.id, self.city.__dict__))

    def test_to_dict(self):
        """Test for to_dict method"""
        self.assertIsInstance(self.city.to_dict(), dict)


if __name__ == "__main__":
    unittest.main()
