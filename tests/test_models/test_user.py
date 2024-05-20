#!/usr/bin/python3
"""Unittest for User class"""

import unittest

import models

from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for the User class"""

    def setUp(self):
        """Set up for the tests"""
        self.user = User()
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        self.user.email = "a@b.com"
        self.user.password = "password"

    def test_init(self):
        """Test the initialization of the User instance"""
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)

    def test_instance(self):
        """Test for User instance"""
        instance = User()
        self.assertIsInstance(instance, User)

    def test_first_name(self):
        """Test for User first_name"""
        instance = User()
        self.assertIsInstance(instance.first_name, str)

    def test_last_name(self):
        """Test for User last_name"""
        instance = User()
        self.assertIsInstance(instance.last_name, str)

    def test_email(self):
        """Test for User email"""
        instance = User()
        self.assertIsInstance(instance.email, str)

    def test_password(self):
        """Test for User password"""
        instance = User()
        self.assertIsInstance(instance.password, str)

    def test_str(self):
        """Test for __str__ method"""
        self.assertEqual(str(self.user), "[User] ({}) {}".format(
            self.user.id, self.user.__dict__))

    def test_to_dict(self):
        """Test for to_dict method"""
        user_dict = self.user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertIsInstance(user_dict["created_at"], str)
        self.assertIsInstance(user_dict["updated_at"], str)
        self.assertIsInstance(user_dict["first_name"], str)
        self.assertIsInstance(user_dict["last_name"], str)
        self.assertIsInstance(user_dict["email"], str)
        self.assertIsInstance(user_dict["password"], str)
        self.assertEqual(user_dict["created_at"],
                         self.user.created_at.isoformat())
        self.assertEqual(user_dict["updated_at"],
                         self.user.updated_at.isoformat())
        self.assertEqual(user_dict["first_name"], self.user.first_name)
        self.assertEqual(user_dict["last_name"], self.user.last_name)
        self.assertEqual(user_dict["email"], self.user.email)
        self.assertEqual(user_dict["password"], self.user.password)

    def test_save(self):
        """Test the save method"""
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_all(self):
        """Test the all method"""
        obj = User()
        objects = models.storage.all()
        self.assertIsInstance(objects, dict)
        self.assertIn("User.{}".format(obj.id), objects)

    def test_new(self):
        """Test the new method"""
        obj = User()
        obj_id = obj.id
        self.assertIn("User.{}".format(obj_id),
                      models.storage.all())


if __name__ == "__main__":
    unittest.main()
