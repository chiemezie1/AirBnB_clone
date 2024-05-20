#!/usr/bin/python3
"""
Unittest for Review class
"""

import unittest

import models

from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for the Review class"""

    def setUp(self):
        """Set up for the tests"""
        self.review = Review()
        self.review.place_id = "opo lopo"
        self.review.user_id = "sñfjefpa"
        self.review.text = "My house"

    def test_init(self):
        """Test the initialization of the Review instance"""
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)

    def test_instance(self):
        """Test for Review instance"""
        instance = Review()
        self.assertIsInstance(instance, Review)

    def test_place_id(self):
        """Test for Review place_id"""
        instance = Review()
        self.assertIsInstance(instance.place_id, str)

    def test_user_id(self):
        """Test for Review user_id"""
        instance = Review()
        self.assertIsInstance(instance.user_id, str)

    def test_text(self):
        """Test for Review text"""
        instance = Review()
        self.assertIsInstance(instance.text, str)

    def test_str(self):
        """Test for __str__ method"""
        self.assertEqual(str(self.review), "[Review] ({}) {}".format(
            self.review.id, self.review.__dict__))

    def test_to_dict(self):
        """Test for to_dict method"""
        self.assertIsInstance(self.review.to_dict(), dict)


if __name__ == "__main__":
    unittest.main()
