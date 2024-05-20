#!/usr/bin/python3
"""
Unittest for State class
"""

import unittest

import models

from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State class"""

    def setUp(self):
        """Set up for the tests"""
        self.state = State()
        self.state.name = "California"

    def test_init(self):
        """Test the initialization of the State instance"""
        self.assertIsInstance(self.state.name, str)

    def test_instance(self):
        """Test for State instance"""
        instance = State()
        self.assertIsInstance(instance, State)

    def test_name(self):
        """Test for State name"""
        instance = State()
        self.assertIsInstance(instance.name, str)

    def test_str(self):
        """Test for __str__ method"""
        self.assertEqual(str(self.state), "[State] ({}) {}".format(
            self.state.id, self.state.__dict__))

    def test_to_dict(self):
        """Test for to_dict method"""
        self.assertIsInstance(self.state.to_dict(), dict)

    def test_all(self):
        """Test for all method"""
        instance = State()
        objects = models.storage.all()
        self.assertIn("State.{}".format(instance.id), objects)

    def test_new(self):
        """Test for new method"""
        instance = State()
        objects = models.storage.all()
        self.assertIn("State.{}".format(instance.id), objects)


if __name__ == "__main__":
    unittest.main()
