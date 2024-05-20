#!/usr/bin/python3
"""
Unittest for Amenity class
"""

import unittest

from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    def setUp(self):
        """Set up for the tests"""
        self.amenity = Amenity()
        self.amenity.name = "Wifi"

    def test_init(self):
        """Test the initialization of the Amenity instance"""
        self.assertIsInstance(self.amenity.name, str)

    def test_instance(self):
        """Test for Amenity instance"""
        instance = Amenity()
        self.assertIsInstance(instance, Amenity)

    def test_name(self):
        """Test for Amenity name"""
        instance = Amenity()
        self.assertIsInstance(instance.name, str)

    def test_str(self):
        """Test for __str__ method"""
        self.assertEqual(str(self.amenity), "[Amenity] ({}) {}".format(
            self.amenity.id, self.amenity.__dict__))

    def test_to_dict(self):
        """Test for to_dict method"""
        self.assertIsInstance(self.amenity.to_dict(), dict)


if __name__ == "__main__":
    unittest.main()
